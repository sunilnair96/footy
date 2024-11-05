### Step 1: Set Up the Project Structure

1. **Directory Structure**:

   - In `C:\Users\sunil\Projects\footy`, create these initial folders to organize your files:
     ```
     footy/
     ├── backend/           # For Express backend API
     ├── frontend/          # For the React or Next.js frontend
     ├── scripts/           # Python scripts for data extraction
     ├── data/              # To store any data files
     └── README.md          # Project overview and setup instructions
     ```

2. **Initialize the Backend**:

   - Navigate to `backend` and initialize a new Node.js project:
     ```bash
     cd C:\Users\sunil\Projects\footy\backend
     npm init -y
     ```
   - Install **Express** and other basic dependencies:
     ```bash
     npm install express cors
     ```
   - Set up an initial Express server file, `server.js`, to start building your API endpoints.

3. **Set Up the Frontend**:

   - In the `frontend` folder, create a new React or Next.js app:
     ```bash
     cd C:\Users\sunil\Projects\footy\frontend
     npx create-next-app .  # If using Next.js
     # or
     npx create-react-app . # If using React
     ```
   - Add **Tailwind CSS** for styling (optional at this stage but recommended as we’ll need it later):
     ```bash
     npm install -D tailwindcss
     npx tailwindcss init
     ```

4. **Linking Frontend and Backend**:
   - To test the connection, start both servers (backend and frontend), ensuring they run on different ports (e.g., 3000 for frontend and 5000 for backend).
   - For now, we can create a simple "Welcome" message on the front page.

### Step 2: Creating the Front Page in the Frontend

1. **Set Up a Basic UI**:

   - Inside your `frontend` folder, go to `pages/index.js` (Next.js) or `src/App.js` (React) and modify it to display a basic front page.
   - For example:

     ```javascript
     import React from "react";

     export default function Home() {
       return (
         <div className="min-h-screen flex items-center justify-center bg-gray-100">
           <h1 className="text-4xl font-bold">
             Welcome to the AFL Fantasy App
           </h1>
           <p className="mt-4">
             Your platform for team building and projections.
           </p>
           <button className="mt-8 px-4 py-2 bg-blue-500 text-white rounded">
             Run Data Extraction
           </button>
         </div>
       );
     }
     ```

2. **Basic Button to Invoke Scripts**:
   - To eventually run Python scripts from this UI, the button can trigger a backend API call that executes the Python program. For now, the button can just display a placeholder message.

Let me know once these initial steps are set up, and we can move forward to creating an API route that will connect the frontend button to Python scripts!
