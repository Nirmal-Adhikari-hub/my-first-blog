volume = int(input('Enter the volume level')) 
if volume < 20:
    print('Its quiet!')
elif 20 <= volume < 40:
    print('Nice for background music')
elif 40 <= volume < 60:
    print('Perfect! I can hear it!')
elif 60 <= volume < 80:
    print('Suits for parties')
elif 80 <= volume < 100:
    print('A bit loud')
else:
    print('My ears are hurting')