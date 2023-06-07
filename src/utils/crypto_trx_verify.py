import time
from django.conf import settings
import requests


def verify_transaction(src, dest, amount, tx_hash, retry=0) -> bool:

    data = {
        'module': 'account',
        'action': 'tokentx',
        'sort': 'desc',
        'address': src,
    }

    response = requests.get(settings.BLOCKCHAIN_EXPELORER, params=data)
    transaction = None

    try:
        transaction = list(filter(lambda x: x.get('hash') == tx_hash,
                                  response.json().get('result')))[0]
    except Exception:

        if retry < 5:
            time.sleep(1)
            retry += 1
            return verify_transaction(src, dest, amount, tx_hash, retry)
        print('tx %s => could not find' % tx_hash)
        return False

    if transaction.get('contractAddress').upper() not in settings.BLOCKCHAIN_TOKENS:
        print('tx %s => token could not verified' % tx_hash)
        return False

    if transaction.get('to').upper() != dest.upper():
        print('tx %s => receiver could not verified' % tx_hash)
        return False

    if int(transaction.get('value')) / 1e18 < int(amount):
        print('tx %s => amount could not verified' % tx_hash)
        return False

    return True
