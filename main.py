import sys
import os
import argparse
from pathlib import Path
from datetime import datetime
import logging
import qrcode
from dotenv import load_dotenv
import validators

# Load environment variables from a .env file
load_dotenv()

# Configuration from environment variables with defaults
QR_DIR = os.getenv('QR_CODE_DIR', 'qr_codes')
QR_FILL_COLOR = os.getenv('FILL_COLOR', 'black')
QR_BACK_COLOR = os.getenv('BACK_COLOR', 'white')

def init_logging():
    """Set up logging to output messages to standard output."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout
    )

def ensure_directory(directory: Path):
    """Create the directory if it does not exist."""
    try:
        directory.mkdir(parents=True, exist_ok=True)
    except Exception as error:
        logging.error(f"Could not create directory {directory}: {error}")
        sys.exit(1)

def validate_url(url: str) -> bool:
    """Check if the given URL is valid."""
    if validators.url(url):
        return True
    logging.error(f"Provided URL is not valid: {url}")
    return False

def create_qr(url: str, output_path: Path, fill_color: str = 'red', back_color: str = 'white'):
    """Generate a QR code image for the URL and save it to a file."""
    if not validate_url(url):
        return

    try:
        qr_instance = qrcode.QRCode(version=1, box_size=10, border=5)
        qr_instance.add_data(url)
        qr_instance.make(fit=True)
        image = qr_instance.make_image(fill_color=fill_color, back_color=back_color)
        with output_path.open('wb') as file:
            image.save(file)
        logging.info(f"QR code generated at {output_path}")
    except Exception as e:
        logging.error(f"Error during QR code generation: {e}")

def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL")
    parser.add_argument('--url', default='https://github.com/Satyabandi20', 
                        help='The URL to encode in the QR code')
    args = parser.parse_args()

    # Initialize logging
    init_logging()
    logging.info(f"Config: QR_DIR={QR_DIR}, QR_FILL_COLOR={QR_FILL_COLOR}, QR_BACK_COLOR={QR_BACK_COLOR}")
    logging.info(f"URL to encode: {args.url}")

    # Prepare filename with a timestamp
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f"QRCode_{current_time}.png"
    output_file = Path.cwd() / QR_DIR / file_name

    # Make sure the QR directory exists
    ensure_directory(Path.cwd() / QR_DIR)

    logging.info("Starting QR code generation...")
    create_qr(args.url, output_file, fill_color=QR_FILL_COLOR, back_color=QR_BACK_COLOR)

if __name__ == "__main__":
    main()
