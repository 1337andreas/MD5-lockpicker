#!/bin/bash
#Script för att cracka MD5-hashar med hashcat.
#Användning: ./hashcatbash1.sh [HASHFIL] [MASK]
#Exempel: ./hashcatbash1.sh output.txt ?d?d?d?d?d?d?d?d?d?d

#Kontrollerar att hashcat är installerat.
if ! command -v hashcat &> /dev/null; then
	echo "Hashcat är inte installerat!"
	echo "Installera med: sudo apt install hashcat"
	exit 1
fi

echo "==== Hashcat MD5 cracker ===="
hashcat --version | head -n 1
echo "============================="

#Standardinställningar

HASH_FILE="${1:-output.txt}"
MASK="${2:-?d?d?d?d?d?d?d?d?d?d}"			#Antal siffror att pröva
HASH_TYPE="0"				#0 = Hash mode MD5
ATTACK_MODE="3"				#3 = Mask-attack

echo "Startar Hashcat..."

#Kör Hashcat

hashcat -m "$HASH_TYPE" -a "$ATTACK_MODE" "$HASH_FILE" "$MASK" -O -w 3 --force
