# SOCIETY DESIGN

This project aims to act as a medium of safety for the residents living in gated communities. Currently building the first version of the project.

### Packages
- database
    - to connect database and backend using bean class (Base class in FastAPI)
- entry
    - to notify residents on visitors entry (residents can choose to allow or deny)
- gatepass
    - generates qr code for pre-approved guests and security can scan it immediately without any further delay
- residents
    - to store resident information and perform crud operations on it

Each package contains (except database):
- init - package initialization
- service - server logic
- schema - defines structure for API requests and responses
- routes - API endpoints (post, get, put, delete)

### API Testing
- resident
    - post - tested and works
    - get - tested and works
    - put - tested and works
    - delete - tested and works
- entry
    - post - tested and works
    - get - tested and works
    - put - tested and works
    - delete - doesn't exist cause entry audit log cannot be deleted for confidentiality
- gatepass - Haven't tested API endpoints for this package cause I need to generate qr and display it as an image on the presentation layer (will do it after building frontend layer)
    - post
    - get
    - put
    - delete - doesn't exist for the same reason as entry

### Flow
Database -> Service layer -> API layer -> Presentation layer

### Completed layers
1) Database layer - Schema design for residents, gatepass and entry_logs
2) Backend layer (Server logic) - resident, gatepass and entry packages
3) API layer (to expose server logic to frontend) - resident, gatepass and entry packages

### Todo layers
1) Presentation layer