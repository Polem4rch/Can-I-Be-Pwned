
![](images/Can I be pwned_2.png)

# Can-I-Be-Pwned
Check if your password is in a Dictionary.

When a leak has been exposed the usual way to find if your account private information has been exposed is searching if your email address is listed within the breach, this tool approach however is different instead of looking your email address, allows you to run your password against a dictionary.


Dictionaries are used for an attack called Brute Forcing;

Definition(s):
  "A method of accessing an obstructed device by attempting multiple combinations of numeric/alphanumeric passwords."
Source(s):
NIST SP 800-101 Rev. 1



If the attacked system has no protection against this type of attack and your password is listed in the used dictionary, any attacker will access your account.

Please use this tool in your systems, for your eyes only.

Usage: python3 canibepwned.py -f dictionary file.txt -p password

For Dictionaries, including leaked databases please refer to:

https://github.com/danielmiessler/SecLists/tree/master/Passwords
