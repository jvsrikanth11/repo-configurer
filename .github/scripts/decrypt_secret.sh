#!/bin/sh

# Decrypt the file
cd $HOME/secrets
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$SECRET_PASS" \
--output $HOME/secrets/app_secrets.json app_secrets.json.gpg