import os, subprocess

project_folder_path = "/home/rshu/Documents/openmrs-module-htmlformentry"
destination_directory = "/home/rshu/Documents/openmrs-module-htmlformentry-all/"
cpg_vis_neo4j_command_path = "/home/rshu/Documents/cpg-vis-neo4j/build/install/cpg-vis-neo4j/bin/cpg-vis-neo4j"
cpg_vis_neo4j_user = "--user=neo4j"
cpg_vis_neo4j_password = "--password=password"


def list_java_files(path):
    f = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if ".java" in name and "Test.java" not in name:
                # print(os.path.join(root, name))
                f.append(os.path.join(root, name))

    # print(f)
    # print(len(f))
    return f


def export_code_to_neo4j(file_list):
    delete_directory_execution = subprocess.run(
        ["rm", "-rf", destination_directory],
        stdout=subprocess.PIPE, text=True)
    print("The exit code was: %d" % delete_directory_execution.returncode)
    print(delete_directory_execution.stdout)

    creat_directory_execution = subprocess.run(
        ["mkdir", destination_directory],
        stdout=subprocess.PIPE, text=True)
    print("The exit code was: %d" % creat_directory_execution.returncode)
    print(creat_directory_execution.stdout)

    for file in file_list:
        print(file)
        copy_execution = subprocess.run(
            ["cp", file, destination_directory],
            stdout=subprocess.PIPE, text=True)
        print("The exit code was: %d" % copy_execution.returncode)
        print(copy_execution.stdout)

    cpg_vis_neo4j_execution = subprocess.run(
        [cpg_vis_neo4j_command_path, cpg_vis_neo4j_user, cpg_vis_neo4j_password, destination_directory],
        stdout=subprocess.PIPE, text=True)
    print("The exit code was: %d" % cpg_vis_neo4j_execution.returncode)
    print(cpg_vis_neo4j_execution.stdout)

    # cpg_vis_neo4j_execution = subprocess.run(
    #     [cpg_vis_neo4j_command_path, cpg_vis_neo4j_user, cpg_vis_neo4j_password, file],
    #     stdout=subprocess.PIPE, text=True)
    # print("The exit code was: %d" % cpg_vis_neo4j_execution.returncode)
    # print(cpg_vis_neo4j_execution.stdout)


def main():
    # traverse all java file in folder
    file_list = list_java_files(project_folder_path)
    export_code_to_neo4j(file_list)


if __name__ == "__main__":
    main()
