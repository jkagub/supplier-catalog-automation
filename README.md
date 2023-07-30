**Online Fruit Store Automation**

![Fruit Store Logo](https://example.com/fruitstorelogo.png)

This project aims to automate the process of updating an online fruit store's catalog information with data provided by suppliers. The system processes images and descriptions received from suppliers and uploads them to the web server that handles the fruit catalog. Additionally, it generates a PDF report summarizing the updates and sends it to the suppliers via email. The project also includes a health check script to monitor system statistics and send alerts in case of issues.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts](#scripts)
- [License](#license)

## Introduction

As an online fruits store, we often receive data from our suppliers in the form of large images (.TIF) and accompanying text descriptions (.txt). The manual process of updating our catalog with this data can be time-consuming and error-prone. This project automates this process, saving time and ensuring accuracy.

The project consists of several Python scripts that handle different aspects of the automation process:

1. `changeImage.py`: Processes supplier images by converting them to JPEG format and resizing them to 600x400 pixels.

2. `supplier_image_upload.py`: Uploads the processed JPEG images to the web server that manages the fruit catalog.

3. `run.py`: Processes text files containing fruit descriptions, converts them to JSON format, and uploads the data to the Django server.

4. `reports.py`: Generates a PDF report summarizing the updates and changes made to the fruit catalog.

5. `report_email.py`: Processes supplier fruit description data, generates the PDF report, and sends it to the suppliers via email.

6. `health_check.py`: Runs in the background, monitoring system statistics such as CPU usage, disk space, available memory, and name resolution. It sends an email alert in case of any issues detected.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x
- Required Python libraries: PIL, requests, reportlab, psutil

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/fruit-store-automation.git
   cd fruit-store-automation
   ```

2. Install the required Python libraries:

   ```
   pip install Pillow requests reportlab psutil
   ```

## Usage

1. Process supplier images:

   ```
   python changeImage.py
   ```

2. Upload processed images to the web server:

   ```
   python supplier_image_upload.py
   ```

3. Process text files and upload data to the Django server:

   ```
   python run.py
   ```

4. Generate and send email with the PDF report:

   ```
   python report_email.py
   ```

5. Monitor system statistics and send email in case of issues:

   ```
   python health_check.py
   ```

## Scripts

- `changeImage.py`: Processes supplier images and converts them to JPEG format.

- `supplier_image_upload.py`: Uploads processed JPEG images to the web server.

- `run.py`: Processes text files containing fruit descriptions, converts them to JSON format, and uploads the data.

- `reports.py`: Generates a PDF report summarizing the updates made to the fruit catalog.

- `report_email.py`: Processes supplier fruit description data, generates the PDF report, and sends it via email.

- `health_check.py`: Monitors system statistics and sends email alerts in case of issues.

## License

This project is licensed under the GNU General Public License version 3.0 - see the [LICENSE](LICENSE) file for details.

For more information on each script and its usage, please refer to the individual script files.

We hope this automation system makes managing more efficient and seamless! Happy automating!
