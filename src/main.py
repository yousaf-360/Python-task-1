from TaskManager import TaskManager
from utils import handle_menu_options

def main(): 
        manager = TaskManager('src/data.json')
        handle_menu_options(manager)
        
if __name__ =='__main__':
        main()
