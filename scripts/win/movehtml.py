
import os
import subprocess

def get_valid_folder():
	base_path = r'D:\xampp\htdocs'
	while True:
		folder = input(f"Enter the htdocs folder name to use (e.g. 'media'): ").strip()
		if not folder:
			print("Folder name cannot be empty.")
			continue
		full_path = os.path.join(base_path, folder)
		if os.path.isdir(full_path):
			return full_path
		else:
			print(f"Folder '{folder}' does not exist under {base_path}. Please try again.")

def main():
    local_folder = get_valid_folder()
    remote_user = 'pi'
    remote_host = 'raspkei.local'
    remote_path = '/home/pi/html'
    
    scp_cmd = f'scp -r "{local_folder}" {remote_user}@{remote_host}:{remote_path}'
    os.system(scp_cmd)
    
if __name__ == "__main__":
	main()