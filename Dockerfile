# ----------- FRONTEND BUILD STAGE -----------
    FROM node:18 AS frontend-build

    WORKDIR /app
    
    # Copy package.json and package-lock.json first (for caching)
    COPY frontend/youtube-downloader-ui/package.json frontend/youtube-downloader-ui/package-lock.json ./
    RUN npm install --legacy-peer-deps
    
    # Copy the rest of the frontend project and build it
    COPY frontend/youtube-downloader-ui ./
    RUN npm run build
    
    # ----------- NGINX STAGE FOR SERVING FRONTEND -----------
    FROM nginx:alpine AS ui
    
    # Copy built frontend files to Nginx's HTML directory
    COPY --from=frontend-build /app/build /usr/share/nginx/html
    
    # Expose frontend port
    EXPOSE 80
    
    # Start Nginx
    CMD ["nginx", "-g", "daemon off;"]
    
    # ----------- BACKEND BUILD STAGE -----------
    FROM python:3.12 AS backend
    
    WORKDIR /app
    
    # Upgrade pip first
    RUN python -m pip install --upgrade pip
    
    # Copy requirements.txt from the root directory
    COPY requirements.txt /app/
    
    # Install dependencies
    RUN pip install --no-cache-dir -r /app/requirements.txt
    
    # Copy the backend code
    COPY backend /app
    
    # Expose Flask port
    EXPOSE 5000
    
    # Run the Flask app
    CMD ["python", "app.py"]
    