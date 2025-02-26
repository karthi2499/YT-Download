# YouTube Downloader

This is a simple YouTube Downloader application built using Flask for the backend and React for the frontend. It allows users to download YouTube videos or extract audio from videos.

## Features
- Download YouTube videos in MP4 format
- Extract and download audio in MP3 format
- Simple and user-friendly interface

## Technologies Used
- **Backend:** Flask, youtube_dl, Flask-CORS
- **Frontend:** React, Tailwind CSS
- **Containerization:** Docker

## Installation
### Prerequisites
Make sure you have the following installed:
```bash
# Install Docker & Docker Compose
https://docs.docker.com/get-docker/
https://docs.docker.com/compose/install/
```

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader

# Build and run the application using Docker
docker-compose up --build
```

### Open the application in your browser:
```bash
http://localhost:3000
```

## API Endpoints
### Download Video/Audio
```http
POST /download
```
**Request Body:**
```json
{
  "url": "<youtube_video_url>",
  "format": "video or audio"
}
```
**Response:** Returns the requested file for download.

## License
```text
MIT License
```

