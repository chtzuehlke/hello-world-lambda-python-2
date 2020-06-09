
openssl ecparam -genkey -name prime256v1 -out key.pem
openssl ec -in key.pem -pubout > pubkey.pem
openssl dgst -binary -sha256 commands.sh  | hexdump
openssl dgst -sha256 -sign key.pem commands.sh > sig
openssl dgst -sha256 -verify pubkey.pem -signature sig commands.sh
