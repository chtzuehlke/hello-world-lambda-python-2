import subprocess

def hello(event, context):
    try:
        subprocess.check_call('openssl ecparam -genkey -name prime256v1 -out /tmp/key.pem',shell=True)
        subprocess.check_call('openssl ec -in /tmp/key.pem -pubout > /tmp/pubkey.pem',shell=True)
        subprocess.check_call('echo "hallo" > /tmp/hallo.txt',shell=True)
        subprocess.check_call('echo "hello" > /tmp/hello.txt',shell=True)
        subprocess.check_call('openssl dgst -sha256 -sign /tmp/key.pem /tmp/hallo.txt > /tmp/hallo.sig',shell=True)
        return {
            "private key":subprocess.check_output('cat /tmp/key.pem',shell=True),
            "public key":subprocess.check_output('cat /tmp/pubkey.pem',shell=True),
            "valid signature check":subprocess.check_output('openssl dgst -sha256 -verify /tmp/pubkey.pem -signature /tmp/hallo.sig /tmp/hallo.txt',shell=True),
            "invalid signature check":subprocess.check_output('openssl dgst -sha256 -verify /tmp/pubkey.pem -signature /tmp/hallo.sig /tmp/hello.txt || true',shell=True),
        }
    
    except subprocess.CalledProcessError as err: #e.g. non-zero exit code
        print(err)
        return repr(err)

    except OSError as err: #e.g. cst inestead cat
        print(err)
        return repr(err)
