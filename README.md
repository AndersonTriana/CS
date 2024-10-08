
![alt text](image.png)

Wireframes: 
https://www.figma.com/design/sG5AY1O4Y5OttS1B57zAXq/Streamlit-Design-System-(Community)?node-id=121-1620&t=uvuh0E8R4DRjGujx-1

# Technical instructions

## Create and activate Python virtual environment
```bash
    python3 -m venv venv
    source venv/bin/activate
```

## Install dependencies
Create file *requirements.txt*

```bash
    pip3 install -r requirements.txt
```

## Run streamlit project

```bash
    chmod +x run_mac.sh
    ./run_mac.sh
    streamlit run main.py
```


# Utilities

## Steps to remove virtual environment
```bash
    deactivate
    rm -rf venv
```

## Common errors:
ERROR: Could not install packages due to an OSError: Could not find a suitable TLS CA certificate bundle, invalid path: /Users/dev/ai/ai-agent-extract-data-from-image/venv/lib/python3.12/site-packages/certifi/cacert.pem
```bash
    (security find-certificate -a -p ls /System/Library/Keychains/SystemRootCertificates.keychain &&  security find-certificate -a -p ls /Library/Keychains/System.keychain) > $HOME/.mac-ca-roots
```
```bash
    export REQUESTS_CA_BUNDLE="$HOME/.mac-ca-roots"
```