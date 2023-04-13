from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp_c
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
import os
import time
import sys
import atexit


print("!!!BEM VINDO!!!\n")

user = input("Digite o user:\n")

email = input("Digite o e-mail:\n")

if("@" not in email):
    print("Email invalido")
    print("Saindo do programa!")
    sys.exit(0)

senha = getpass("Digite a senha:\n")
os.system('cls||clear')
print("Aguarde!")



PATH = ("","/usr/local/bin/geckodriver")[sys.platform.startswith("linux")]





opt = Options()
#opt.add_argument("--headless")
opt.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Firefox(options=opt)
#driver.set_window_size(1366,6000)
os.system('cls||clear')


def kill():
    driver.quit()



def login():
    gg = False
    driver.get("https://discord.com/login")

    try:
        WebDriverWait(driver, 60).until(
            Exp_c.visibility_of_element_located((By.ID, "uid_5")))
        gg = True

       
    except TimeoutError:
        print("Timeout")
        pass
    if gg:
        driver.find_element(By.ID, "uid_5").send_keys(email)
        driver.find_element(By.ID, "uid_7").send_keys(senha)

        driver.find_element(By.CLASS_NAME, "button-1cRKG6").click()

        time.sleep(15)
        if "Login or password is invalid." in driver.find_element(By.TAG_NAME, "body").text:
            print("Login ou senha invalidos")
            return False
        else:
            print("Carregando...")
            WebDriverWait(driver, 60).until(
                Exp_c.visibility_of_element_located((By.CLASS_NAME, "title-338goq")))
            p_page = driver.find_element(By.TAG_NAME, "body").text
            if user in p_page:
                print("Sucesso!\nEstamos na sua conta!!!")
                return True
            else:
                return False
    else:
       print("Nao foi possivel logar")
       return False



def list_server():
    elements = driver.find_elements(By.CSS_SELECTOR,"[aria-label=Servers]")
    lists = [i.find_elements(By.CLASS_NAME,"wrapper-3kah-n") for i in elements]
    dict_serv = {k:[i.get_attribute("aria-label"),i] for k in range(len(lists)) for i in lists[k] }

    return dict_serv
            

#members fnc
def list_members():
    time.sleep(5)
    try:
        driver.find_element(By.CSS_SELECTOR,'[aria-label="Show Member List"]').click()

    except NoSuchElementException:
        pass
    finally:
        
        lista_mem=driver.find_element(By.CLASS_NAME, "members-3WRCEx").find_element(By.CSS_SELECTOR, '[aria-label="Members"]')


        members = lista_mem.find_elements(By.CLASS_NAME, "member-2gU6Ar")
        dict_tags = {}
        time.sleep(2)
        for i in range(len(members)):
            members[i].click()

            WebDriverWait(driver, 10).until(Exp_c.visibility_of_element_located((By.CLASS_NAME, "userPopoutOuter-1OHwPL")))
            tag = driver.find_elements(By.CLASS_NAME, "discrimBase-v65kTs")[0].text
            name = driver.find_elements(By.CLASS_NAME, "username-3JLfHz")[0].text
            print(i)

            print(tag)
            dict_tags.update({i:[name, tag]})


        return dict_tags    

def send_msg(id):
    try:
        act = ActionChains(driver)
        driver.find_elements(By.CLASS_NAME, "wrapper-3kah-n")[0].click()
        driver.find_elements(By.CLASS_NAME, "searchBarComponent-3N7dCG")[0].click()
        driver.find_elements(By.CLASS_NAME, "input-3r5zZY")[0].send_keys(id)

        driver.find_elements(By.CLASS_NAME, "result-u66Ywh")[0].click()
        time.sleep(2)
        driver.find_elements(By.CLASS_NAME, "slateTextArea-27tjG0")[1].click()

        
        act.key_down(Keys.SUBTRACT).key_up(Keys.SUBTRACT).send_keys(" test").perform()

        act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    except:
        pass


if __name__ == "__main__":
    atexit.register(kill)

    while True:

        

        print("""
-------------------------------
------!!!BOT INICIADO!!!-------
-------------------------------
⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠖⠶⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡞⠉⠀⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀
⠀⢤⡀⠀⢰⣋⠦⡠⢤⡀⠀⢀⡤⢤⡰⣻⡇⠀⢀⣠⠄
⠀⠈⣿⣶⣾⣎⢟⣀⡄⣹⠀⣮⢠⢀⣹⣱⣷⣶⣿⡇⠀
⠀⠀⢿⣿⣿⣟⠺⠿⣿⢦⠀⡤⢾⡷⠗⢹⣿⣿⣿⠀⠀
⠀⠀⠘⢿⣿⣿⢩⡆⣡⣞⠉⣱⣌⢠⡯⣿⣿⡿⠋⠀⠀
⠀⠀⠀⡠⢜⣻⣬⢾⣮⡟⣿⠛⡵⡫⣣⣿⣣⢤⡀⠀⠀
⢀⣔⠛⢭⣾⣿⣿⣧⠹⣭⣿⣭⠞⣽⣿⣿⣷⣭⠙⣢⡄
⣾⡏⣉⣭⣽⡽⢿⣿⣷⣀⣾⣄⣼⣿⣯⢿⣯⣭⣉⡹⣿
⣽⣿⣿⠉⣠⡞⠉⣸⠟⣻⠿⣟⠛⣧⠈⢳⣆⡉⡿⣿⣿
⢳⣿⢏⣾⣿⢃⣾⣯⣤⣿⣀⢽⣤⣼⣷⡜⣿⣿⣉⣿⡿
⠀⠀⠿⠟⣿⣏⣟⠏⡜⣿⠿⣿⢫⠘⣿⣸⣿⠣⠿⠃⠀
⠀⠀⠀⠀⠈⠛⠁⠈⠷⠞⠀⠻⠾⠃⠈⠛⠁⠀⠀⠀⠀
-------------------------------
-------------------------------
""")

        print("Logando...\n-------------------------------")

        if login():
            break

        else:

            resp = input("Tentar novamente: (S/N")
            if resp.upper() == "S" or resp == "":
                login()
               
            else:
                   sys.exit(0)
    os.system('cls||clear')               
    
    while True:
        resp = input("""----Opções:----
Entrar em servidor(ES)    Lista de servidores(LS)
Enviar mensagem(MS)
                  
                  \n\n\nSair(Q)\n"""
                ).upper()
        if resp=="Q":
            os.system('cls||clear')               

            sys.exit(0)
        elif resp=="MS":
            id_ins = input("Digite o id: ")
            send_msg(id_ins)
        
        elif resp=="LS":
            os.system('cls||clear')

            s_ret = list_server()
            print("\n")
            for key in s_ret:
                print(f"{key}) {s_ret[key][0]}")


            n_r=input("\nO que deseja fazer agora?\nEntrar em servidor(aperte o numero da lista)\nVoltar(V)\nSair(Q)\n")
            os.system('cls||clear')

            if(n_r.upper()=="Q"):
                sys.exit(0)
            elif n_r.isdigit:
                print("\nentrando...\n")
                s_ret[int(n_r)][1].click()
                
                os.system('cls||clear')

                n_s=input(f"Pronto!\nEntramos no {s_ret[int(n_r)][0]}\nO que fazer agora:\nListar Membros(LM)\nsair(Q)\n").upper()
                
                


                if n_s =="LM":
                    ml = list_members()
                    inps = input("Salvar tags?(Y/N): ")
                    if inps.upper() == "Y":
                        ar = open("tags.txt","a+")
                        for key in ml:
                            ar.write(f'{key}, {ml[key][0]}, {ml[key][1]}\n')
                        ar.close()
                        print("Tags salvas")
                    for key in ml:
                        print(f"{key}) {ml[key][0]}")
                    
                    
                    