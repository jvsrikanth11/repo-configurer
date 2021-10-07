#!/bin/sh

# Decrypt the file
cd .github/secrets
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$SECRET_PASS" \
--output .github/secrets/app_secrets.json app_secrets.json.gpg