# Name: Keegan Smith, Jack Smith, Noah Gruber, Logan Schuster
# email: smith6kg@mail.uc.edu, smit4jk@mail.uc.edu, grubernw@mail.uc.edu, schustlt@mail.uc.edu 
# Assignment Title: Final Project
# Due Date: 12/07/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates we can decrypt AES, navigate UC campus, and use Pillow
# Citations: 
# Anything else that's relevant: 

import json
from cryptography.fernet import Fernet
from PIL import Image

'''
we need to decrypt the location data
@param encrypted_data: the encryption data (TeamsAndEncryptedMessages.json)
@param: english_file_path: the english txt file (english-2.txt)
@returns: the decrypted locations, as a dictionary.
'''
def decrypt_location_data(encrypted_data, english_file_path):
    #open and read the english-2.txt
    with open(english_file_path, 'r', encoding='utf-8') as english_file:
        english_text = english_file.readlines()

    #match up indices, store in a dictionary (decrypted_location{})
    decrypted_location = {}
    #add error handling in case one doesn't work
    for team_member, indices in encrypted_data.items():
        try:
            decrypted_words = [english_text[int(index)].strip() for index in indices]
            decrypted_location[team_member] = decrypted_words
        except IndexError:
            decrypted_location[team_member] = f"Error decrypting indices for {team_member}"

    return decrypted_location


'''
the key needs to be a FILE (key_file) in order to decrypt with Fernet.
@param: none
@returns: A key file. If none exists in the project, generate a new one.
'''
def load_key():
    #if there is not a key file, generate a new one.
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        #you'll likely never see this happen, but it did once. it was awesome.
        print("Key file not found. Generating a new key.")
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

'''
time to bring it all together
@param: none
@returns: the dictionary from decrypt_location_data, with a helpful message.
'''
def decrypt_and_display():
    key = load_key()
    
    with open("TeamsAndEncryptedMessagesForDistribution.json", "r") as file:
        teams_and_messages = json.load(file)

    encrypted_data_path = "EncryptedGroupHints Fall 2023 Section 001.json"
    with open(encrypted_data_path, 'r') as file:
        encrypted_data = json.load(file)

    decrypted_location = decrypt_location_data(encrypted_data, "english-2.txt")
    print("\nDecrypted Location:")
    for team_member, location in decrypted_location.items():
        print(f"{team_member}: {location}")
