# Homework-7

## QR Code Linking to My GitHub Homepage
![QR Code](qr_codes/QRCode_20250331114556.png)

## Log of QR Code Creation
![Log Screenshot](qr_codes/qr_logs.png)

```bash
@Satyabandi20 ➜ /workspaces/homework7 (main) $ docker login -u satya6644
Password: 
WARNING! Your password will be stored unencrypted in /home/codespace/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credential-stores

Login Succeeded

@Satyabandi20 ➜ /workspaces/homework7 (main) $ docker push satya6644/my-qr-app:latest
The push refers to repository [docker.io/satya6644/my-qr-app]
465cdc6df049: Pushed 
50bd2b1fc3f9: Pushed 
bbf89bf9b6a8: Pushed 
007aa5f8f275: Pushed 
fff28c72bf47: Pushed 
0bd20682cfd1: Pushed 
e4614f580cbd: Pushed 
cf8fb9711e2f: Pushed 
0495f9cd4e58: Pushed 
d215e887b4c2: Pushed 
latest: digest: sha256:f8f40189dffb9d0e2689e293b52153584bb2df2f5350a0586223cd7d9bb8ac4b size: 2405

@Satyabandi20 ➜ /workspaces/homework7 (main) $ docker run --name qr-generator my-qr-app
2025-03-31 11:40:58,950 - INFO - Config: QR_DIR=qr_codes, QR_FILL_COLOR=black, QR_BACK_COLOR=white
2025-03-31 11:40:58,950 - INFO - URL to encode: https://github.com/Satyabandi20
2025-03-31 11:40:58,950 - INFO - Starting QR code generation...
2025-03-31 11:40:58,977 - INFO - QR code generated at /app/qr_codes/QRCode_20250331114058.png

@Satyabandi20 ➜ /workspaces/homework7 (main) $ docker logs qr-generator
2025-03-31 11:40:58,950 - INFO - Config: QR_DIR=qr_codes, QR_FILL_COLOR=black, QR_BACK_COLOR=white
2025-03-31 11:40:58,950 - INFO - URL to encode: https://github.com/Satyabandi20
2025-03-31 11:40:58,950 - INFO - Starting QR code generation...
2025-03-31 11:40:58,977 - INFO - QR code generated at /app/qr_codes/QRCode_20250331114058.png
