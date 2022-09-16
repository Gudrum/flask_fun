# Password Hashing

Obviously, it is of utmost importance that we do not store plaintext user passwords in the event that our database is compromised. Below is a diagram of how "password hashing" works.

## Registration/Storing Data
```mermaid
sequenceDiagram
  Client->>Server: User submits registration form
  Server->>Server: Validate form
  Server->>Server: Take plaintext password and encrypt it using an encryption algorithm/library like bcrypt
  Server->>Database: Trigger INSERT query and store all data with encrypted password
  Database->>Server: Notify server that INSERT has been committed
  Server->>Client: Redirect or success action
```

## Login/Verifying Password
```mermaid
sequenceDiagram
  Client->>Server: User submits login form
  Server->>Database: Request relevant user info including encrypted password from database
  Database->>Server: Send requested info back to server
  Server->>Server: Validate form
  Server->>Server: Take plaintext password from form and encrypt it using the same algorithm used in registration
  Server->>Server: Compare newly encrypted form password against encrypted password from db
  Server->>Client: Respond with success/failure action
```