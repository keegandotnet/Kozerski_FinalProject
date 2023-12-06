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

def get_team_info(json_file_path, team_name):

    """
    Retrieve the encrypted data from a JSON file.

    @param json_file_path: Name of JSON file
    @param team_noame: Name of the team
    @returns: Encrypted data for the specified team
    """
    
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    if team_name in data:
        return data[team_name][0]
    
    

def decrypt_movie_name(encrypted_data, key):
    """
    Decrypt an encryption using Fernet
    
    @param encrypted_data: The encrypted data
    @param key: need the original key for decryption
    @returns: The decrypted data
    """
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data.encode())
    return decrypted_data.decode()
