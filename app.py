import yt_dlp
import logging
from flask_cors import CORS
from flask import Flask, request, jsonify
from youtubeParams import ydl_opts

logging.basicConfig(
    filename='ytdownload.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
CORS(app)


@app.route('/api/download/', methods=['POST'])
def download():
    try:
        data = request.json
        param = ydl_opts[data['file_formate']]

        url = data['url']
        try:
            logger.info(f"Starting download: {url}")
            with yt_dlp.YoutubeDL(param) as ydl:
                ydl.download([url])
            logger.info(f"Download complete: {url}")

        except yt_dlp.utils.DownloadError as e:
            logger.error(f"Download error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")

        return jsonify({'message': 'Started Downloading'})
    except Exception as e:
        return jsonify({'error': e.__str__()}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)
