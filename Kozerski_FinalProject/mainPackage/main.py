# Name: Keegan Smith, Jack Smith, Noah Gruber, Logan Schuster
# email: smith6kg@mail.uc.edu, smit4jk@mail.uc.edu, grubernw@mail.uc.edu, schustlt@mail.uc.edu 
# Assignment Title: Final Project
# Due Date: 12/07/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates we can decrypt AES, navigate UC campus, and use Pillow
# Citations: 
# Anything else that's relevant: 

if __name__ == "__main__":
    import json
    from moviePackage.movie import *
    from functionsPackage.functions import *
    json_file_path = "TeamsAndEncryptedMessagesForDistribution.json"
    team_name = "Kozerski"
    key = 'r0J5NgEGqsxufa0af1zLpy8DaNhQ9C9ur6PBWqialy4='.encode()
    encrypted_data = get_team_info(json_file_path, team_name)
    print("Encrypted Data:", encrypted_data)
    movie_name = decrypt_movie_name(encrypted_data, key)
    print("Decrypted Movie Name:", movie_name)

    decrypt_and_display()
    display_resized_image(r"..\assetsPackage\results-edit.jpg")
