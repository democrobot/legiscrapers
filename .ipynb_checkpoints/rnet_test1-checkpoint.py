import asyncio
import os
# Correct import for rnet's impersonation enum
from rnet import Client, Impersonate 

async def download_pdf(pdf_url: str, output_filename: str):
    """
    Downloads a PDF file from a given URL using rnet.

    Args:
        pdf_url (str): The URL of the PDF file to download.
        output_filename (str): The name of the file to save the PDF as.
    """
    print(f"Attempting to download PDF from: {pdf_url}")

    # Initialize the rnet client, mimicking a Chrome browser
    # Use Impersonate.Chrome[Version] as per rnet's documentation
    # I'll use a recent Chrome version for the example.
    # You can find the full list in rnet's GitHub documentation.
    client = Client(impersonate=Impersonate.Chrome127) # Example: Impersonate Chrome 127

    try:
        # Make an asynchronous GET request to the PDF URL
        response = await client.get(pdf_url)

        # Check if the request was successful (status code 200)
        response.raise_for_status() # Raises an HTTPStatusError for bad responses (4xx or 5xx)

        # Check if the content type is indeed PDF (optional but good practice)
        content_type = response.headers.get("Content-Type", "")
        if "application/pdf" not in content_type:
            print(f"Warning: Expected 'application/pdf' but got '{content_type}'. Still attempting to save.")

        # Write the content of the response to a file in binary write mode
        with open(output_filename, 'wb') as f:
            f.write(response.content)

        print(f"Successfully downloaded PDF to: {output_filename}")

    except Exception as e:
        print(f"An error occurred during download: {e}")
    finally:
        # Close the client session to release resources
        await client.close()

async def main():
    # Replace this with the actual URL of the PDF you want to download
    # Example: A public PDF from a government site or academic paper
    pdf_url = "https://www.palegis.us/legislation/bills/text/DOC/2025/0/HR0134/PN1045" # A sample dummy PDF URL
    output_filename = "downloaded_document.docx"

    await download_pdf(pdf_url, output_filename)

if __name__ == "__main__":
    # Run the main asynchronous function
    asyncio.run(main())
