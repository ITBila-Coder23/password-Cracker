#!/usr/bin/env python3
"""
wordlist_attack.py — Educational wordlist attack against a SHA-256 hash.

Usage:
    python3 wordlist_attack.py --hash <sha256> --wordlist wordlist.txt
"""
import argparse
import hashlib
import sys
import time

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Educational wordlist attack simulation")
    parser.add_argument("--hash", required=True, help="Target SHA-256 hash (hex)")
    parser.add_argument("--wordlist", required=True, help="File with candidate passwords (one per line)")
    parser.add_argument("--show-every", type=int, default=1000, help="Show progress every N attempts")
    args = parser.parse_args()

    target = args.hash.strip().lower()
    path = args.wordlist

    start = time.time()
    tried = 0
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                pwd = line.rstrip("\n")
                tried += 1
                if tried % args.show_every == 0:
                    elapsed = time.time() - start
                    rate = tried / (elapsed + 1e-9)
                    print(f"tried={tried} rate={rate:.1f}/s last='{pwd[:40]}'")
                if sha256_hex(pwd) == target:
                    elapsed = time.time() - start
                    print(f"*** FOUND *** password='{pwd}' after {tried} attempts (time {elapsed:.2f}s)")
                    return 0
        print("[!] Password not found in wordlist.")
        return 2
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {path}")
        return 1
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting.")
        return 130

if __name__ == "__main__":
    sys.exit(main())
