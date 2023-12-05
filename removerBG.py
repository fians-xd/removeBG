import requests
import os
from tqdm import tqdm

# Warna
h  = ('\x1b[0;32m') # hijau gelap
ht = ('\x1b[32;1m') # hijau terang
b  = ('\x1b[0;36m') # biru gelap
bt = ('\x1b[36;1m') # biru terang
m  = ('\x1b[31;1m') # merah
p  = ('\x1b[37;1m') # putih
h  = ('\x1b[30;1m') # hitam
k  = ('\x1b[33;1m') # kuning
kt = ('\x1b[1;33m') # kuning terang

# Logo
___logo___ = (f"""
{kt}________                                             _________________
{kt}___{ht}  __ \___________ ____________   ______           {kt}___{ht}  __ )_  ____/
{kt}__{ht}  /_/ /  _ \_  __ `__ \  __ \_ | / /  _ \ {k}__{ht}______ {kt}__{ht}  __  |  / __
{kt}_{bt}  _, _//  __/  / / / / / /_/ /_ |/ //  __/ {k}_{bt}/{bt}_____{bt}/ {kt}_{bt}  /_/ // /_/ /
{bt}/_/ |_| \___//_/ /_/ /_/\____/_____/ \___/           /_____/ \____/
{kt}[{p}•{kt}]{ht}———————————————————————————————————
{m}[{ht}>{m}] {p}Auth {m}: {p}Yan-XD                     {h}𝙸𝚗𝚝𝚛𝚘𝚍𝚞𝚌𝚝𝚒𝚘𝚗{k}:{h}𝙷𝚊𝚗𝚢𝚊 𝚜𝚎𝚋𝚞𝚊𝚑 𝚝𝚘𝚘𝚕𝚜 𝚜𝚎𝚍𝚎𝚛𝚑𝚊𝚗𝚊 𝚢𝚊𝚗𝚐 𝚍𝚒𝚋𝚞𝚊𝚝 𝚍𝚊𝚛𝚒 𝚙𝚢𝚝𝚑𝚘𝚗
{m}[{ht}>{m}] {p}Git  {m}: {p}@sofian246                     {h}𝚋𝚎𝚛𝚝𝚞𝚓𝚞𝚊𝚗 𝚞𝚗𝚝𝚞𝚔 𝚔𝚎𝚋𝚞𝚝𝚞𝚑𝚊𝚗 𝚎𝚍𝚒𝚝𝚒𝚗𝚐 𝚏𝚘𝚝𝚘.!! 𝙷𝚙𝚙𝚢 𝙴𝚍𝚒𝚝𝚒𝚗𝚐 {m}◔ {bt}◡{m}◔
{m}[{ht}>{m}] {p}Fb   {m}: {p}fb.com/sofian.nasution.146
{kt}[{p}•{kt}]{ht}———————————————————————————————————{p}
""")

def remove_background(image_path, output_filename, api_key):
    # API endpoint
    api_url = "https://api.remove.bg/v1.0/removebg"

    # Open image file
    image_file = open(image_path, 'rb')

    # Create output directory if it doesn't exist
    output_folder = "hasil"
    os.makedirs(output_folder, exist_ok=True)

    # Send POST request to the API
    response = requests.post(
        api_url,
        files={'image_file': image_file},
        data={'size': 'auto'},
        headers={'X-Api-Key': api_key},
        stream=True
    )

    # Get content length from response headers
    file_size = int(response.headers.get('Content-Length', 0))

    # Set up tqdm progress bar
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc="\x1b[36;1mProcessing.\x1b[31;1m!\x1b[33;1m")

    # Save the result if successful
    if response.status_code == requests.codes.ok:
        output_path = os.path.join(output_folder, output_filename)
        with open(output_path, 'wb') as out:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    out.write(chunk)
                    progress_bar.update(len(chunk))
        progress_bar.close()
        print("\n\x1b[0;32mBackground removed successfully.!\x1b[37;1m", output_path)
    else:
        progress_bar.close()
        print("\x1b[0;32mError:\x1b[37;1m", response.status_code, response.text)

# Input manual
os.system('clear')
print(___logo___)
input_image = input("\x1b[0;32mMasukkan path gambar input\x1b[33;1m:\x1b[37;1m ")
output_filename = input("\x1b[0;32mMasukkan nama file di folder\x1b[33;1m:\x1b[37;1m ")
print(" ")
api_key = "QwHL7To7SUmVxDcnveHBQcyF"

remove_background(input_image, output_filename, api_key)
