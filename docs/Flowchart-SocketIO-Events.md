BanditGUI - SocketIO Events

This Mermaid flowchart illustrates the SocketIO events and their corresponding actions in the BanditGUI application. The application is built using Flask and SocketIO, and it interacts with three main classes: **SSHManager**, **PasswordManager**, and **ChatManager**.

```mermaid
flowchart TD
    A["Start Flask Application"] --> B["Initialize SocketIO"]
    B --> C["Create Instances of SSHManager, PasswordManager, and ChatManager"]
    C --> D["Handle Root Route '/'"]
    D --> E["Render 'index.html' with BANDIT_LEVELS"]
    
    F["SocketIO Event: 'connect_ssh'"] --> G{"Username and Password Provided?"}
    G -->|No| H["Emit SSH Error: 'Please provide both username and password'"]
    G -->|Yes| I["Retrieve Username, Password, Session ID"]
    
    J["SocketIO Event: 'disconnect_ssh'"] --> K["SSHManager.disconnect()"]
    
    M["SocketIO Event: 'execute_command'"] --> N["SSHManager.execute_command()"]
    N --> O["Emit Command Result"]
    
    P["SocketIO Event: 'retrieve_password'"] --> Q["PasswordManager.get_password()"]
    Q --> R["Emit Retrieved Password"]
    
    S["SocketIO Event: 'chat_message'"] --> T["ChatManager.generate_response()"]
    T --> U["Emit Chat Response"]
```
