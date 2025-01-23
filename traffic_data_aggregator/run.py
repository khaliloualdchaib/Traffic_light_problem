from app import create_app  # Import the create_app function

# Create a Flask application instance
app = create_app()

if __name__== '__main__':
    app.run(host="0.0.0.0", port=5002)