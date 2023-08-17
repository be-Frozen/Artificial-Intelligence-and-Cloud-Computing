import docker

class ClusterManager:
    def __init__(self):
        self.client = docker.from_env()
        self.containers = []
        self.volume_name = "my_volume"
        self.load_existing_containers() 

    def load_existing_containers(self):
        existing_containers = self.client.containers.list(all=True)
        self.containers.extend(existing_containers)
        print("Loading existing containers......  done.")

    def create_cluster(self, num_containers):
        for _ in range(num_containers):  # Use _ for unused loop variable
            container_name = input("Enter the name for the container: ")
            image_name = input("Enter the image name for the container: ")
            self.create_container(container_name, image_name)
        print("Containers created!")
        print(f"Currently has {len(self.containers)} containers.\n")  # Use f-string for formatting

    def create_container(self, container_name, image_name):
        container = self.client.containers.run(
            image_name,
            name=container_name,
            volumes={self.volume_name: {'bind': '/path/in/container', 'mode': 'rw'}},
            detach=True,
            tty=True,         
            stdin_open=True   
        )
        #print(f"Container type: {type(container)}, Container name: {container.name}")
        self.containers.append(container)
        print(f"Container {container_name} created and mounted to volume.")
    
    def list_cluster(self):
        if not self.containers:
            print("There is no container!\n")
        else:
            print("Current cluster containers:")
            for container in self.containers:
                print(f"Container name: {container.name}, Container status: {container.status}")
            print("")

    def run_command_in_container(self, container_name, command):
        container = self.client.containers.get(container_name)
        if container.status != "running":
            print(f"Container '{container_name}' is not running. Starting...")
            container.start()
        exec_result = container.exec_run(command)
        print(f"Output from '{command}' in '{container_name}':\n{exec_result.output.decode()}")

    def stop_cluster(self, container_name):
        container = self.client.containers.get(container_name)
        if container.status != "exited":
            print(f"Container '{container_name}' is Stopping...")
            container.stop()
        else:
            print(f"Container '{container_name}' is already stopped.")

    def delete_all_containers(self):
        for container in self.containers:
            container.remove()
        self.containers = []
        print("Deleting all containers...\n")

if __name__ == "__main__":
    cm = ClusterManager()

    while True:
        print("Available commands:")
        print("1. Create Cluster")
        print("2. List Cluster")
        print("3. Run Command in Cluster")
        print("4. Stop Cluster")
        print("5. Delete All Containers")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num_containers = int(input("Enter the number of containers to create: "))
            cm.create_cluster(num_containers)
        elif choice == "2":
            cm.list_cluster()
        elif choice == "3":
            container_name = input("Enter the name of the container: ")
            command = input("Enter the command to run in the container: ")
            cm.run_command_in_container(container_name, command)
        elif choice == "4":
            container_name = input("Enter the name of the container you want to stop: ")
            cm.stop_cluster(container_name)
        elif choice == "5":
            cm.delete_all_containers()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")
