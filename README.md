# ALX Webstack - Todo Application (Full-Stack)

---

## 🚀 Project Overview

This project is a full-stack Todo application developed as part of my **ALX Webstack - Portfolio Project**. It demonstrates a complete web development workflow, integrating a clean, responsive frontend with a robust Python backend for persistent data storage.

The application allows users to manage their daily tasks: add new todos, mark them as complete, filter by active/completed/all, delete individual todos, and clear all completed tasks. All data is stored in a SQLite database via the backend, ensuring persistence even after the browser is closed.

---

## ✨ Features

* **Add New Todos:** Easily create new tasks.
* **Mark as Complete:** Toggle todo status with a click.
* **Delete Todos:** Remove tasks individually.
* **Filter Todos:** View All, Active, or Completed tasks.
* **Clear Completed:** Remove all finished tasks with one action.
* **Data Persistence:** All todo items are stored in a database via the backend.
* **Responsive Design:** Adapts to different screen sizes.
* **Light/Dark Theme Toggle:** Switch between themes for user preference.

---

## 🛠️ Technologies Used

### Frontend
* **HTML5:** Structure of the web pages.
* **CSS3 (Sass):** Styling and responsiveness.
* **JavaScript (ES6+):** Client-side logic and interaction with the backend API.


### Backend
* **Python 3:** Core programming language.
* **Flask:** Lightweight web framework for building RESTful APIs.
* **Flask-SQLAlchemy:** ORM (Object Relational Mapper) for database interactions.
* **SQLite3:** Simple, file-based database for persistent storage.
* **Flask-CORS:** Handles Cross-Origin Resource Sharing for seamless frontend-backend communication.

---

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* [Git](https://git-scm.com/)
* [Python 3.x](https://www.python.org/downloads/)
* (Optional but Recommended for Frontend) [Node.js & npm](https://nodejs.org/en/download/) for running a local server like `serve`.

### Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/pat6h/ALX-Webstack-TodoApp.git]
    cd ALX-Webstack-TodoApp
    ```

2.  **Backend Setup:**
    Navigate into the `backend` directory, set up a virtual environment, install dependencies, and run the Flask server.

    ```bash
    cd backend
    python -m venv venv
    # Activate virtual environment
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    pip install -r requirements.txt
    python app.py
    ```
    The backend server should start on `http://127.0.0.1:5000/`. Keep this terminal running.

3.  **Frontend Setup:**
    Open a **new** terminal window and navigate into the `frontend` directory.

    ```bash
    cd ../frontend # Go back to root, then into frontend
    # OR: cd ALX-Webstack-TodoApp/frontend
    ```
    * **Option A (Recommended: Use a Local Server):**
        If you have Node.js installed, install `serve` globally:
        ```bash
        npm install -g serve
        ```
        Then, run the server from the `frontend` directory:
        ```bash
        serve
        ```
        It will provide a URL like `http://localhost:3000` (or similar) to open in your browser.

    * **Option B (Simple File Open - May have CORS issues in some browsers):**
        Simply open the `index.html` file directly in your browser.
        (e.g., `file:///path/to/ALX-Webstack-TodoApp/frontend/index.html`)

---

## ⚙️ Backend API Endpoints

The backend exposes the following RESTful API endpoints:

* `GET /todos`: Retrieve all todo items.
* `POST /todos`: Create a new todo item. Request body: `{ "text": "New todo content" }`.
* `PUT /todos/<id>`: Update an existing todo item. Request body: `{ "completed": true }` or `{ "text": "Updated content" }`, `{ "order": 1 }`.
* `DELETE /todos/<id>`: Delete a specific todo item.
* `DELETE /todos/clear-completed`: Delete all completed todo items.

---

## 💡 How to Use

1.  Ensure both the backend (Python `app.py`) and frontend (`index.html` via `serve` or directly) are running.
2.  Open the frontend URL in your browser.
3.  Type a task in the input field and press Enter to add it.
4.  Click the circle next to a task to mark it as complete.
5.  Click the 'X' icon to delete a task.
6.  Use the filter options (All, Active, Completed) at the bottom.
7.  Click "Clear Completed" to remove all finished tasks.

All changes will be reflected in your `todos.db` file in the `backend/` directory.

---

## ✍️ Author

**Ayoub Zeroual**
* [My GitHub Profile](https://github.com/pat6h)

---

## 🙏 Acknowledgements

* **ALX Webstack Program:** For the opportunity and guidance on this portfolio project.
