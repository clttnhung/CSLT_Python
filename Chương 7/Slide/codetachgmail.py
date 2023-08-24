gmail='caolethituyetnhung@gmail.com '
acong=gmail.find('@')
daucach=gmail.find('',acong)
host=gmail[acong+1:daucach]
print(host)