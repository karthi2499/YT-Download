import React, { useState } from "react";
import axios from "axios";
import { TextField, Button, Container, Typography, MenuItem, Select } from "@mui/material";

const VideoDownloader = () => {
  const [url, setUrl] = useState("");
  const [fileFormat, setFileFormat] = useState("video");
  const [message, setMessage] = useState("");

  const handleDownload = async () => {
    if (!url) {
      setMessage("Please enter a valid YouTube URL.");
      return;
    }

    try {
      setMessage("Downloading...");
      const response = await axios.post("/api/download/", {
        url,
        file_formate: fileFormat,
      });      

      setMessage(response.data.message || "Download started!");
    } catch (error) {
      console.error("Download error:", error);
      setMessage(error.response?.data?.error || "Download failed!");
    }
  };

  return (
    <Container maxWidth="sm" style={{ marginTop: "50px" }}>
      <Typography variant="h4" align="center">YouTube Downloader</Typography>

      <TextField
        fullWidth
        label="Enter YouTube URL"
        variant="outlined"
        margin="normal"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <Select
        fullWidth
        value={fileFormat}
        onChange={(e) => setFileFormat(e.target.value)}
        style={{ marginBottom: "15px" }}
      >
        <MenuItem value="video">Video</MenuItem>
        <MenuItem value="audio">Audio</MenuItem>
      </Select>

      <Button variant="contained" color="primary" fullWidth onClick={handleDownload}>
        Download
      </Button>

      {message && <Typography variant="subtitle1" style={{ marginTop: "20px", textAlign: "center" }}>{message}</Typography>}
    </Container>
  );
};

export default VideoDownloader;
