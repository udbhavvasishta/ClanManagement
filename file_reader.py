import os

class FileReader:
    def read_clan_war_data(self):
        clan_war = os.getenv('LEADERSHIP')
        coleaders = False
        elders = False
        coleaders_list = []
        elders_list = []
        with open(clan_war, 'r') as file:
            while True:
                line = file.readline().strip()
                if line == 'Co-Leaders:':
                    coleaders = True
                if line == 'Elders:':
                    coleaders = False
                    elders = True
                
                if coleaders:
                    coleaders_list.append(line)
                elif elders:
                    elders_list.append(line)
        
        return coleaders_list, elders_list


                
                        

