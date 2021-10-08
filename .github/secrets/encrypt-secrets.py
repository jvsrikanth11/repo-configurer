#! /usr/bin/env nix-shell
#! nix-shell -i python
#! nix-shell -p "python3.withPackages (p: [ p.pynacl ])"

from base64 import b64encode
from nacl import encoding, public

def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

public_key = "++BHjPifxMH2Y8p3K6Y7mM94OwW0EGkkgZQesDXeKF8="

print("APP_KEY=", encrypt(public_key, "abc@123"))
