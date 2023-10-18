#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Port Scanner"""
# version: 0.1.2
# license: MIT
# author: Anthony Pagan
# repo: https://github.com/get-tony/pyutils

import asyncio
import random
import argparse
from typing import List


async def scanner(ip: str, port: int, timeout: float = 0.5) -> None:
    """Scan a single port asynchronously.

    Args:
        ip: The IP address to scan.
        port: The port number to scan.
        timeout: The timeout for each port scan.

    Returns:
        None.
    """
    try:
        _, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port), timeout=timeout
        )
        print(f"{ip}:{port} Connected")
        writer.close()
        await writer.wait_closed()
    except asyncio.TimeoutError:
        pass
    except ConnectionRefusedError:
        print(f"{ip}:{port} Connection refused")
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Error {ip}:{port} {exc}")


def scan(
    ips: List[str],
    ports: List[int],
    timeout: float = 0.5,
    randomize: bool = False,
) -> None:
    """Scan a range of ports on a list of IP addresses.

    Args:
        ips: The list of IP addresses to scan.
        ports: The list of port numbers to scan.
        timeout: The timeout for each port scan.
        randomize: Whether to randomize the order of port scans.

    Returns:
        None.
    """
    tasks = []
    for ip in ips:
        for port in ports:
            tasks.append(scanner(ip, port, timeout=timeout))

    if randomize:
        random.shuffle(tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))


def main() -> None:
    """Parse command line arguments and scan ports."""
    parser = argparse.ArgumentParser(
        description="Scan ports on a list of IP addresses"
    )
    parser.add_argument(
        "ips",
        metavar="ip",
        type=str,
        nargs="+",
        help="IP addresses to scan",
    )
    parser.add_argument(
        "-p",
        "--ports",
        metavar="port",
        type=int,
        nargs="+",
        default=list(range(1, 65536)),
        help="ports to scan (default: all)",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        metavar="timeout",
        type=float,
        default=0.5,
        help="Timeout for each scan (default: 0.5 seconds)",
    )
    parser.add_argument(
        "-r",
        "--randomize",
        action="store_true",
        help="Randomize the order of port scans",
    )
    args = parser.parse_args()

    ips: List[str] = args.ips
    ports: List[int] = args.ports
    timeout: float = args.timeout
    randomize: bool = args.randomize

    scan(ips, ports, timeout=timeout, randomize=randomize)


if __name__ == "__main__":
    main()
