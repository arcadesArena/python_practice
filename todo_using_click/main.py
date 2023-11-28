import click

PRIORITIES = {
    "o":"Optional",
    "l":"Low",
    "m":"Medium",
    "h":"high",
    "c":"critcal"
}


@click.command()
@click.argument("file",type=click.Path(exists=False),required=0)
@click.option("-n","--name",prompt="Enter the title",help="title of the task")
@click.option("-d","--description",prompt="Enter the description",help="description of the task")
@click.option("-p","--priority",prompt="Enter priority",type=click.Choice(PRIORITIES.keys()),default="m")
def add_task(name,description,priority,file):
    file = file if file is not None else "todo_list.txt"
    with open(file,"a+") as f:
        f.write(f"{priority}::{name}::{description};;\n")

@click.command()
@click.argument("idx",type=int,required=1)
@click.argument("file",type=click.Path(exists=False),required=0)
def delete_task(idx,file):
    file = file if file is not None else "todo_list.txt"
    with open(file,"r") as f:
        tasks = f.read().splitlines()
        tasks.pop(idx)
    with open(file,"w") as f:
        f.write("\n".join(tasks))
        f.write("\n")

@click.command()
@click.option("-p","--priority",type=click.Choice(PRIORITIES.keys()))
@click.argument("file",type=click.Path(exists=False),required=0)
def list_tasks(priority,file):
    file = file if file is not None else "todo_list.txt"
    with open(file,"r") as f:
        tasks = f.read().splitlines()
    if priority == None:
        for i,task in enumerate(tasks):
            # p,t,d = task[:-2].split("::")
            print(f"{str(i).rjust(3,'0')}: {task}")
    else:
        for i,task in enumerate(tasks):
            if priority == task.split("::")[0]:
                p,t,d = task[:-2].split("::")
                print(f"{str(i).rjust(3,'0')}: {task}")

@click.group
def commands():
    pass

commands.add_command(add_task)
commands.add_command(delete_task)
commands.add_command(list_tasks)

if __name__=='__main__':
    commands()