class user_interface:
    def run(self,lst_file: list):
        """
        lst_file is a list containing all the filename in the template folder
        This function let you start the interace, allowing the user to have the
        programm executed the task needed
        """
        lst_size = len(lst_file)
        while True:
            cmpt = 0
            command_panel = "Veuiller entrer le nombre correspondant à l'action attendu. Tout autre actions ne correspondant pas au choix offert arrêtera l'application \n"
            for filename in lst_file:
                command_panel += f"{cmpt} Créer {filename}\n"
                cmpt += 1
            command_panel += f"{cmpt} Créer tout les pdfs\n{cmpt+1} Exporter les dates pour google calendar\n{cmpt+2} Tout exécuter\n"
            answ = input(command_panel)
            if answ.isdigit():
                answ_int = int(answ)
                if answ_int == lst_size:
                    print("do all md")
                elif answ_int < lst_size:
                    print(lst_file[int(answ)])
            else:
                break
        