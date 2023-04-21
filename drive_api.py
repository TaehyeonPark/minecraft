from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from pathlib import Path

from json import load

# do not share
token = {
  "type": "service_account",
  "project_id": "able-starlight-384404",
  "private_key_id": "b17074aa3bf74452eb1d0c2836d8159f7e87bef4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDhyJPNlIro1fzF\nfdGUv1GjCe2Vgqpf0RSutORE9KhWTJvW/uRpRtHD9RsVkkwWB4qOFFqnYloAyUqe\nHSWQbiHM58KWXBRWRGHXM8yCPEzF6f3IRNPMFccWv+2Twq8oBenbBvqQw8vgLe1D\n8+461I6bmKT6m7oaz49hw7Qpero/DN+iQM0ywouoYk5AfrkF4JN/wUUvDnGubFz9\nosa0Yy7NxbOkH+oHFCxpS7Aa22DJv1YoJ/pKRxmanO4nyYP0QKd4GZx3RWe9f2KI\nCjI03+JkoF/cETnXlviF9Q5Z7tkIDi3tVekJfAxTvpYCYccN5A9PwP4Xyr8JbeKV\nZPJtQfjZAgMBAAECggEACXnQDjQ6Qjxc3/MAXURMSlHr2TcDLINLYWuxGt3DxN9x\nOOw4rNxuiFFcoiKiM9h8LatYBKdhjJ/mFE232mBs5bsiVQonRlmXW59OaXbbaAEC\niCmvU+TkFqXWdDma/UyGPI2F7ZZyE4YJ66yspmZuV8RnxCbOADsO0vUSNh1y/Jtb\nBnlXibhGoFCbgbNKJS1WYfZjWdI54uqBCevpTe0ehxetes+L1tWXtKL38ezx4niV\nxUxoWDCFelgmx9O3dGUTXA0g1UEALnj2w9NqOjnSp6W9iOOqbPmdV7A3FhaoZKyS\nqhDjGyALOE7GPrXhbSyiZTsoyesgIPrz6xwJ0SFDSQKBgQD0ltO+msIgPA9MdNf8\nXgDCXy/kZ0sh46RrzLKdnpJS2Ww3bxVpxA4YcxF+apDYOaVU1VXKtFLxjwdlRvoK\neCZBWPybbaX7pg0A9KY4cxpxioGl37wvh69FXItfYgiSFlcsbhg6UKLPrFtv2uUt\noH1jZVCMsi/ETOve3d4o/Q7HrQKBgQDsUSaZUJWtlx3U86VDGq7C59BoETDu+2A3\nJKgxehw09cXo30VbOr8a97NGl/Zph9IhKmkLpnC4al4wyR+VxNZuZK/unrI6q/q2\nYr4c4RYB6R1cJ6+eVUyzvRG/4SqwLhOVPTM+AiFiORhb89Gn/QIxEhVqLSn7tCuO\n5zsf42sLXQKBgQDs3R/kJ2U16FP8e+8q1DIyChKMQ8gL4rO5PbwATq9vkmVtbaM0\nEQyBevYHEdaBv5mwBQWXT3g/vH6yAsFk4CRUBoRjVRV4Fb/kHAjZBAcoy7RwWbKZ\n6PHA3zWNwpeAOihju5604qA5M7Y9JaPpwtGLL3OJPYpqtP97jit2UFM+5QKBgQCI\nQhJbfFeRi/yreQDlPFFgGIHWP3NTmKXVpdFFFf+FmeDPcU1wWOMwDXrVTXHLT4Ed\nlnKTQRjlfI9q2czYcnKhnHTExcRGiDs7RpwP0sj5uQwwwsFELjLXwECnvpD6nNa1\nyl/tdRUCqaEeA+vzTLMi0CaA3iHC/BPRhgpVTK/AEQKBgDauQ3DMcHpJ7Ar71Owe\n25wkTIwAbIGP/sYMEzMWuezC8In/+OhmAxg+Q6CA07CrCGI1v6+CbNIDN9hSvge+\n1IPojfnIY2MZdmzpMsd3UjWEjE/RzlbUDOj1FzxINSqEDq+oib7SJi0pU+vubans\nt6JtlX97o1dxwODKji1uj0dp\n-----END PRIVATE KEY-----\n",
  "client_email": "minecraft@able-starlight-384404.iam.gserviceaccount.com",
  "client_id": "100748309186219847110",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/minecraft%40able-starlight-384404.iam.gserviceaccount.com"
}

SCOPES = ['https://www.googleapis.com/auth/drive']
root = "1A1E5wDIboYrYEuQJXsJ-wF9OZ1Cd7Qj6"

def ls(): # load_service
    credentials = service_account.Credentials.from_service_account_info(
        token,
        scopes=SCOPES,
    )
    service = build('drive', 'v3', credentials=credentials)
    return service

def upload_file(service, parent: str, filename: Path):
    file_metadata = {
        'name': filename.name,
        'parents': [parent]
    }
    media = MediaFileUpload(filename, mimetype='video/mp4')
    file = service.files().create(supportsAllDrives=True, 
            body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

def load_list(service, dir: str, mimeType = None):
    q = f"'{dir}' in parents"
    if mimeType is not None:
        q += f" and mimeType = '{mimeType}'"

    results = service.files().list(includeItemsFromAllDrives=True, supportsAllDrives=True, 
                q=q, pageSize=1000, fields="nextPageToken, files(id, name, mimeType)").execute()
    folders = results.get('files', [])
    return folders

def create_dir(service, parent: str, name: str):
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent]
    }
    file = service.files().create(body=file_metadata, supportsAllDrives=True, fields='id').execute()
    folderid = file.get('id')
    return folderid

def autocheck(service, username: str, platform: str, filename: Path, logger): #autoupload
    folders = load_list(service, root, "application/vnd.google-apps.folder")
    folderid = None
    for f in folders:
        if f["name"] == f"{username}.{platform}":
            folderid = f["id"]
            break
    
    if folderid is None:
        logger.info(f"Creating folder {username}.{platform}")
        folderid = create_dir(service, root, f"{username}.{platform}")
    logger.info(f"Uploading {filename.name}")
    fileid = upload_file(service, folderid, filename)
    logger.info(f"Uploaded {filename.name}")
    filename.unlink()
    return fileid

