# Password Cracker Simulation (Educational)

**Purpose:**  
This is an educational, simulated password "cracker" intended only for learning how brute-force and wordlist attacks work in a *controlled environment*.  
**Do not use** these tools on real accounts, systems, or against any targets you do not own or have explicit permission to test.

## Files
- `brute_force.py` — simple brute-force simulation. Small charset and max length defaults to avoid misuse.
- `wordlist_attack.py` — tries passwords from a wordlist file against a target hash.
- `sample_hashes.txt` — example SHA-256 hashes to test with (contains a hash for "abc").
- `requirements.txt` — minimal dependencies (none required for basic usage).
- `LICENSE` — permissive notice.

## Quick usage (local machine):
1. Open a terminal in this folder.
2. Run a brute-force demonstration (safe defaults):
   ```
   python3 brute_force.py --hash <SHA256_HASH_OF_TARGET> 
   ```
   Example using provided sample hash (for password "abc"):
   ```
   python3 brute_force.py --hash $(cat sample_hashes.txt)
   ```
3. Or run the wordlist attack:
   ```
   python3 wordlist_attack.py --hash <HASH> --wordlist wordlist.txt
   ```

## Notes & safety
- Default charset is lowercase letters and digits and max length 3 (configurable).
- This project is for education only. Respect laws and ethics.

