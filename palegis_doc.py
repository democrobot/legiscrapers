import asyncio
from rnet import Impersonate, Client


async def main():
    # Build a client
    client = Client(impersonate=Impersonate.Firefox136)

    # Use the API you're already familiar with
    response = await client.get("https://www.palegis.us/legislation/bills/text/DOC/2025/0/HR0134/PN1045")
    
    # Print the response
    with open('document.doc', 'wb') as f:
            f.write(await response.bytes())


if __name__ == "__main__":
    asyncio.run(main())