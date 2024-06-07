alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g',
          'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']


def change(rawtext,shift,to_do):
    new_text=""
    if to_do=="decrypt":
       shift*=-1
    for char in rawtext:
        if char in alphabet:
          index=alphabet.index(char)
          new_index=(index+shift)%26
          new_text+=alphabet[new_index]
        else:
           new_text+=char
    if to_do=="encrypt" :
      print(f"The Encrypted text-> {new_text}")
    else:
       print(f"The Decrypted text-> {new_text}")
    return new_text



ends=False
last_output=None
while not ends:
  if last_output is None:
    message=input("Enter your message: ").lower()
  else:
    message=last_output
  to_do=input('What do you want to do to your message encryption or decryption\nType "encrypt" for encryption or "decrypt" for decryption: ')
  shift=int(input("How much you want your texts to be shifted: "))

  last_output=change(message,shift,to_do)
  
  again=input('Do you want to continue the same message or new message this time or end it?\n Type "continue" or "new" or "end: ')
  if again=="end":
     ends=True
     print("Here we end the process")
  elif again=="new":
     last_output=None




