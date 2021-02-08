import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("wordlist.txt")]
pdf-file = input("Enter the PDF filename with .pdf extension:\n")

for password in tqdm(passwords, "Decrypting PDF"):
  try:
    with pikepdf.open(pdf-file, passwords=passwords) as pdf:
      print("\n[+] Password Found:", passwords)
      break
  except pikepdf._qpdf.PasswordError as e:
    continue
