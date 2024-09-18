import asyncio

TIMEOUT = 60


class EchoUDPProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print(f"Received {message} from {addr}")
        # Echoing back the received message
        self.transport.sendto(data, addr)


async def run_server():
    print("Starting UDP server")
    # Bind to localhost on UDP port 8888
    loop = asyncio.get_running_loop()
    transport, _ = await loop.create_datagram_endpoint(
        lambda: EchoUDPProtocol(), local_addr=("127.0.0.1", 8888)
    )

    try:
        await asyncio.sleep(TIMEOUT)  # Run for 1 hour
    finally:
        print("Server Shutdown due to Timeout")
        transport.close()


if __name__ == "__main__":
    asyncio.run(run_server())
