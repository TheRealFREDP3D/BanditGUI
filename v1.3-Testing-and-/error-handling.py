# app/utils/error_handler.py
import logging
import traceback
import functools
import json
from flask import jsonify, current_app, request
from typing import Callable, Any, Dict, Optional

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("bandit_ctf_helper")

# Error codes
class ErrorCodes:
    AUTH_ERROR = 1001
    SSH_CONNECTION_ERROR = 2001
    COMMAND_EXECUTION_ERROR = 2002
    DATABASE_ERROR = 3001
    LEVEL_DATA_ERROR = 4001
    VALIDATION_ERROR = 5001
    SERVER_ERROR = 9001

class APIError(Exception):
    """Base class for API errors"""
    def __init__(
        self, 
        message: str, 
        code: int, 
        status_code: int = 400, 
        details: Optional[Dict] = None
    ):
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details
        super().__init__(self.message)

    def to_dict(self) -> Dict:
        """Convert error to dictionary for JSON response"""
        error_dict = {
            "error": True,
            "code": self.code,
            "message": self.message
        }
        if self.details:
            error_dict["details"] = self.details
        return error_dict

def api_error_handler(f: Callable) -> Callable:
    """Decorator to handle API errors and return proper JSON responses"""
    @functools.wraps(f)
    def decorated(*args, **kwargs) -> Any:
        try:
            return f(*args, **kwargs)
        except APIError as e:
            # Log the error
            logger.error(f"API Error: {e.message} (Code: {e.code})")
            if e.details:
                logger.error(f"Error details: {json.dumps(e.details)}")
            
            # Return JSON error response
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
        except Exception as e:
            # Log unexpected errors
            error_details = {
                "exception": str(e),
                "traceback": traceback.format_exc(),
                "endpoint": request.path,
                "method": request.method,
            }
            
            logger.error(f"Unexpected error: {str(e)}")
            logger.error(f"Error details: {json.dumps(error_details)}")
            
            # Return generic error for production
            if current_app.config.get("DEBUG", False):
                # In debug mode, return detailed error
                response = jsonify({
                    "error": True,
                    "code": ErrorCodes.SERVER_ERROR,
                    "message": str(e),
                    "traceback": traceback.format_exc()
                })
            else:
                # In production, return generic error
                response = jsonify({
                    "error": True,
                    "code": ErrorCodes.SERVER_ERROR,
                    "message": "An unexpected error occurred"
                })
            
            response.status_code = 500
            return response
    
    return decorated

# Example usage in routes
# app/routes/terminal.py
from flask import Blueprint, request, jsonify
from app.services.terminal_service import terminal_service
from app.utils.error_handler import api_error_handler, APIError, ErrorCodes

bp = Blueprint('terminal', __name__)

@bp.route('/execute', methods=['POST'])
@api_error_handler
def execute_command():
    data = request.json
    
    # Validate request data
    if not data or 'command' not in data or 'session_id' not in data:
        raise APIError(
            message="Invalid request: missing required fields",
            code=ErrorCodes.VALIDATION_ERROR,
            details={"required": ["command", "session_id"]}
        )
    
    try:
        output, level_completed = terminal_service.execute_command(
            data.get('user_id'), 
            data.get('session_id'), 
            data.get('command')
        )
        
        return jsonify({
            "output": output,
            "levelCompleted": level_completed
        })
    except Exception as e:
        raise APIError(
            message=f"Command execution failed: {str(e)}",
            code=ErrorCodes.COMMAND_EXECUTION_ERROR,
            status_code=500
        )
