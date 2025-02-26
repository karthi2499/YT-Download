# Use an official Node.js image
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first (for caching)
COPY youtube-downloader-ui/package.json youtube-downloader-ui/package-lock.json ./

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy the rest of the frontend project
COPY youtube-downloader-ui ./

# Build the React app
RUN npm run build

# Use Nginx to serve the React build
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
