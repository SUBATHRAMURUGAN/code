ltr=input()
list1=('a','e','i','o','u','A','E','I','O','U')
list2=('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z')
if(ltr in list1):
  print("Vowel")
elif(ltr in list2):
  print("Consonant")
else:
  print("invalid")
