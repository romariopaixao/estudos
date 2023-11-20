from werkzeug.security import generate_password_hash, check_password_hash


print('###################  SENHA ORIGINAL  #################################')
senha = 'renan123'
print(senha)
print('###################  SENHA CRIPTOGRAFADA  #################################')
senha_criptografada  = generate_password_hash(senha)
print(senha_criptografada)
print('###################  COMPARA SE A SENHA CRIPTOGRAFADA É A MESMA QUE FOI DIGITADA  #################################')
print(check_password_hash(senha_criptografada, senha))