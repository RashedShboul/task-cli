import sys
from task_tracker import add_task, list_tasks, delete_task, change_status, update_description


def print_usage():
    print("Usage:")
    print("  add <description>")
    print("  mark-in-progress <task_id>")
    print("  mark-done <task_id>")
    print("  delete <task_id>")
    print("  list <all|todo|in-progress|done>")
    print("  update <task_id> <new_description>")

def main():
    if len(sys.argv) < 2:
        print('Missing argument')
        print_usage()
    
    command = sys.argv[1]
    if command == 'help':
        print_usage()
        
    elif command == 'add' and len(sys.argv) == 3:
        add_task(sys.argv[2])
    
        
    elif command == 'mark-in-progress' and len(sys.argv) == 3:
        change_status(sys.argv[2], 'in-progress')
        
    elif command == 'mark-done' and len(sys.argv) == 3:
         change_status(sys.argv[2], 'done')
    
    elif command == 'delete' and len(sys.argv) == 3:
        delete_task(sys.argv[2])
        
    elif command == 'list' and len(sys.argv) == 2:
            list_tasks('all')
            
    elif command == 'list' and len(sys.argv) == 3 and sys.argv[2] in ['all', 'done', 'todo', 'in-progress']:
            list_tasks(sys.argv[2])
            
    elif command == 'update' and len(sys.argv) == 4:
        update_description(sys.argv[2], sys.argv[3])
    
    else:
        print('Invalid command or missing arguments')
        print_usage() 
        
        
if __name__ == "__main__":
    main()
        
        