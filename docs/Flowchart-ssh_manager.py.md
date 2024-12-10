# BanditGUI - Flowchart

## ssh_manager.py

Here's a flowchart diagram representation of the SSH management workflow using the `SSHManager` class:

```mermaid
flowchart TD
    A["Initialize SSHManager"] --> B["Connect Method Called"]
    B --> C{Existing Connection?}

    C -->|Yes| D["Close Existing Connection"]
    D --> F["Create New SSH Client"]

    C -->|No| F

    F --> G["Set Host Key Policy"]
    G --> H["Store Credentials"]
    H --> I["Return True"]

    J["Execute Command Method Called"] --> K{Connection Exists?}
    K -->|No| L["Raise Exception"]

    K -->|Yes| M["Execute Command"]
    M --> N{"Capture Output/Error"}
    N --> O["Adjust Line Endings"]
    O --> P["Return Result"]

    Q["Disconnect Method Called"] --> R{Connection Exists?}
    R -->|No| S["Do Nothing"]

    R -->|Yes| T["Close Connection"]
    T --> U["Remove Session Data"]
```

This flowchart outlines the steps taken during the execution of methods in the `SSHManager` class, including connection management, command execution, and disconnection procedures.
