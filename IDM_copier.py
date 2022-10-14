# 1. Read in Google Sheet
from contextlib import nullcontext
import pandas as pd
df = pd.read_excel('Deployment sheet for IDM and SLS.xlsx', 'IDM')
completed_rm_commands = df['dag deletion command'].to_list()
# print(completed_rm_commands[0])
# completed_rm_commands.pop(0)
# completed_rm_commands.pop(0)
# print(completed_rm_commands[0])


# 2. Copy GCS Bucket Path
rm_command = "gsutil rm "
dag_files = df['DAG file'].to_list()
config_paths = df['config'].to_list()
remove_commands = []

# 3. Append gsutil rm command + path + py file name
count = 0
for path in config_paths:
    if count >= 2:
        bucket_path = path.split()[4].split('config')[0]
        dag_rm_command = rm_command + bucket_path + dag_files[count]
        # print(dag_rm_command)
        remove_commands.append(dag_rm_command)
    count += 1

df_export = pd.DataFrame(data=remove_commands)
df_export.to_excel("generated.xlsx")

# 4. Test if accurate
# completed_rm_commands.sort()
# remove_commands.sort()

# if partially_completed == partial_remove_commands:
#     print("Lists Match")

# 4. Export to sheets
