
import subprocess
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def main():
    pi_user = input('Enter your Raspberry Pi username: ')
    pi_host = input('Enter your Raspberry Pi hostname (default: raspkei.local): ') or 'raspkei.local'
    source_dir = r'D:\xampp\htdocs'
    pi_html_dir = f'/home/{pi_user}/html'

    logging.info(f"This will sync all files from {source_dir} to {pi_html_dir} on {pi_host} using rsync.")
    confirm = input('Type YES to continue: ')
    if confirm.strip().upper() != 'YES':
        logging.info('Aborted.')
        sys.exit(0)

    # Step 1: Create html directory on Pi user's home
    create_html_cmd = f'ssh {pi_user}@{pi_host} "mkdir -p {pi_html_dir}"'
    logging.info(f'Running: {create_html_cmd}')
    result = subprocess.run(create_html_cmd, shell=True)
    if result.returncode != 0:
        logging.error('Failed to create html directory on Raspberry Pi.')
        sys.exit(1)

    # Step 2: Use rsync to sync files
    rsync_cmd = (
        f'rsync -avz --delete "{source_dir}/" {pi_user}@{pi_host}:{pi_html_dir}/'
    )
    logging.info(f'Running: {rsync_cmd}')
    result = subprocess.run(rsync_cmd, shell=True)
    if result.returncode != 0:
        logging.error('Rsync failed. Please check your connection and try again.')
        sys.exit(1)

    logging.info('All files synced to html folder on Raspberry Pi.')

if __name__ == "__main__":
    main()
