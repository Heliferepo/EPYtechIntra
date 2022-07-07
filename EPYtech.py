from sys import stderr
from typing import Any
import requests
import json

EPITECH_TIRANA      = 'AL/TIR'
EPITECH_BRUXELLES   = 'BE/BRU'
EPITECH_COTONOU     = 'BJ/COT'
EPITECH_BORDEAUX    = 'FR/BDX'
EPITECH_LA_REUNION  = 'FR/RUN'
EPITECH_LILLE       = 'FR/LIL'
EPITECH_LYON        = 'FR/LYN'
EPITECH_MARSEILLE   = 'FR/MAR'
EPITECH_MONTPELLIER = 'FR/MPL'
EPITECH_MOULINS     = 'FR/MLN'
EPITECH_MULHOUSE    = 'FR/MLH'
EPITECH_NANCY       = 'FR/NCY'
EPITECH_NANTES      = 'FR/NAN'
EPITECH_NICE        = 'FR/NCE'
EPITECH_PARIS       = 'FR/PAR'
EPITECH_RENNES      = 'FR/REN'
EPITECH_STRASBOURG  = 'FR/STG'
EPITECH_TOULOUSE    = 'FR/TLS'
EPITECH_BERLIN      = 'DE/BER'
EPITECH_BARCELONA   = 'ES/BAR'

EPITECH_BACHELOR_CLASSIC  = 'bachelor/classic'
EPITECH_BACHELOR_TEK2ED   = 'bachelor/tek2ed'

EPITECH_CODAC_CODE_AND_GO = 'Code-And-Go'
EPITECH_CODAC_DEV_AND_GO  = 'Dev-And-Go'
EPITECH_CODAC_DATA_AND_GO = 'Data-And-Go'

EPITECH_GLOBAL_DIGITAL    = 'globaldigital'

EPITECH_MASTER_CLASSIC    = 'master/classic'

EPITECH_MSC               = 'msc'
EPITECH_PRE_MSC           = 'premsc'

EPITECH_WAC               = 'webacademie'
EPITECH_WAC_AMBITION_FEMININE = 'wac-ambition-feminine'

EPITECH_CODAC1 = 'Codac1'

EPITECH_DIGITAL1 = 'Digital1'
EPITECH_DIGITAL2 = 'Digital2'
EPITECH_DIGITAL4 = 'Digital4'

EPITECH_MSC3 = 'msc3'
EPITECH_MSC4 = 'msc4'
EPITECH_MSC5 = 'msc5'

EPITECH_TEK1 = 'tek1'
EPITECH_TEK2 = 'tek2'
EPITECH_TEK3 = 'tek3'
EPITECH_TEK4 = 'tek4'
EPITECH_TEK5 = 'tek5'

EPITECH_WAC1 = 'wac1'
EPITECH_WAC2 = 'wac2'

class EPYtechIntraError(Exception):

    def __init__(self, message: str = 'undefined') -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return 'EPYtechIntraError(message: ' + str(self) + ')'

class EPYtechIntra:

    AUTOLOGIN_FILE_PATH: str = '.intra-epitech.autologin'
    INTRA: str = 'https://intra.epitech.eu/'
    AUTOLOGIN: str = ''

    def get_payload(self) -> str:
        return self.INTRA + self.AUTOLOGIN + '/'

    def _make_request(self, req, get: bool = True, use_json: bool = True) -> Any:
        req = self.get_payload() + req
        if use_json:
            req += '&format=json' if req.count('?') else '?format=json'
        try:
            rep = requests.get(req) if get is True else requests.post(req)
            rep.raise_for_status()
            return rep
        except Exception as e:
            raise EPYtechIntraError(
                    'Could not access EpitechIntra with autologin:\n' +
                    json.dumps({ 'request': req, 'answer': rep.text, 'status_code': rep.status_code, 'error': str(e)},
                    indent=4))

    def save_autologin(self) -> None:
        try:
            with open(self.AUTOLOGIN_FILE_PATH, 'w+') as f:
                f.write(self.AUTOLOGIN)
        except Exception as e:
            print('EPYtechIntraWarning: Could not save new Autologin in file: '
                    + str(e), file=stderr)

    def update_autologin(self) -> None:
        rep = self._make_request('admin/autolog/generate', get=False)
        self.AUTOLOGIN = json.loads(rep.text)['autologin']
        self.save_autologin()

    def get_autologin(self, by_req: bool = False) -> str:
        if by_req is True:
            return json.loads(self._make_request(f'admin/autolog'))['autologin']
        else:
            return self.AUTOLOGIN

    def trombi(self, location: List[str], prom: List[str], year: List[str], offset: int = 0) -> List[Any]:
        year = '|'.join(year)
        prom = '|'.join(prom)
        location = '|'.join(location)
        req = f'user/filter/user?format=json&location={location}&year={year}&active=true&promo={prom}&offset={offset}'
        res = json.loads(self._make_request(req).text)
        while offset + len(res['items']) < res['total']:
            res['items'].extend(self.trombi(location, prom, year, offset + len(res['items']))['items'])
        return res

    def get_module(self, year: str | int, module: str, instance: str) -> Any:
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/').text)

    def get_registered_module(self, year: str | int, module: str, instance: str) -> List[Any]:
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/registered').text)

    def get_activity(self, year: str | int, module: str, instance: str, activity: str) -> Any:
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}').text)

    def get_activity_appointments(self, year: str | int, module: str, instance: str, activity: str) -> Any:
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/rdv').text)

    def get_project(self, year: str | int, module: str, instance: str, activity: str) -> Any:
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/project').text)

    def get_project_registered(self, year: str | int, module: str, instance: str, activity: str) -> Any:
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/project/registered').text)

    def get_project_unregistered(self, year, module, instance, activity):
        return self._make_request(f'module/{year}/{module}/{instance}/{activity}/project/exportunregistered', use_json=False).text.split('\n')

    def get_project_files(self, year, module, instance, activity):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/project/file/').text)

    def get_event_registered(self, year, module, instance, activity, event):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/{event}/registered').text)

    def get_internship(self):
        return json.loads(self._make_request('stage'))

    def get_user(self, user):
        return json.loads(self._make_request(f'user/{user}').text)

    def get_user_print(self, user):
        return json.loads(self._make_request(f'/user/{user}/print').text)

    def get_user_netsoul(self, user):
        return json.loads(self._make_request(f'user/{user}/netsoul').text)

    def get_partners(self, user):
        return json.loads(self._make_request(f'user/binome').text)

    def course_filter(self):
        return json.loads(self._make_request(f'course/filter').text)

    def get_planning(self):
        return json.loads(self._make_request(f'planning/load').text)

    def get_dashboard(self):
        return json.loads(self._make_request('').text)

    def __init__(self, autologin=None):
        if autologin is None:
            try:
                f = open(self.AUTOLOGIN_FILE_PATH, 'r')
                self.AUTOLOGIN = f.read()
            except Exception as e:
                raise EPYtechIntraError("Error: " + str(e) + '\n' +
                        "You did not provide any autologin and we could not find one in " +
                        self.AUTOLOGIN_FILE_PATH)
        else:
            self.AUTOLOGIN = autologin
            self.save_autologin()
