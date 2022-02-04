import sys, requests, json

class EPYtechIntraError(Exception):

    def __init__(self, message='undefined'):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return 'EPYtechIntraError(message: ' + str(self) + ')'


class EPYtechIntra:

    AUTOLOGIN_FILE_PATH = '.intra-epitech.autologin'
    INTRA = 'https://intra.epitech.eu/'
    AUTOLOGIN = ''

    def get_payload(self):
        return self.INTRA + self.AUTOLOGIN + '/'

    def _make_request(self, req, get=True, json=True):
        req = self.get_payload() + req
        if format_json:
            req += '&format=json' if req.count('?') else '?format=json'
        try:
            rep = request.get(req) if get is True else requests.post(req)
            rep.raise_for_status()
            return rep
        except Exception as e:
            raise EPYtechIntraError(
                    'Could not access EpitechIntra with autologin:\n' +
                    json.dumps({ 'request': req, 'answer': rep.text, 'status_code': rep.status_code, 'error': str(e)},
                    indent=4))

    def update_autologin(self):
        rep = self._make_request('admin/autolog/generate', get=False)
        self.AUTOLOGIN = json.loads(rep.text)['autologin']
        try:
            with open(self.AUTOLOGIN_FILE_PATH, 'w+') as f:
                f.write(self.AUTOLOGIN)
        except Exception as e:
            print('EPYtechIntraWarning: Could not save new Autologin in file: '
                    + str(e), file=sys.stderr)

    def get_autologin(self, by_req=False):
        if by_req is True:
            return json.loads(self._make_request(f'admin/autolog'))['autologin']
        else:
            return self.AUTOLOGIN

    def trombi(self, location, prom, year, offset='0'):
        year = '|'.join(year)
        prom = '|'.join(prom)
        location = '|'.join(location)
        return json.loads(self._make_request(f'user/filter/user?format=json&location={location}&year={year}&active=true&promo={prom}&offset={offset}').text)

    def get_module(self, year, module, instance):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/').text)

    def get_registered_module(self, year, module, instance):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/registered').text)

    def get_activity(self, year, module, instance, activity):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}').text)

    def get_activity_appointments(self, year, module, instance, activity):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/rdv').text)

    def get_project(self, year, module, instance, activity):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/project').text)

    def get_project_registered(self, year, module, instance, activity):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/project/registered').text)

    def get_project_unregistered(self, year, module, instance, activity):
        return self._make_request(f'module/{year}/{module}/{instance}/{activity}/project/exportunregistered', json=False).text.split('\n')

    def get_project_files(self, year, module, instance, activity):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/project/file/').text)

    def get_event_registered(self, year, module, instance, activity, event):
        return json.loads(self._make_request(f'module/{year}/{module}/{instance}/{activity}/{event}/registered').text)

    def get_internship(self):
        return json.loads(self._make_request('stage'))

    get_stage = get_internship

    def get_user(self, user):
        return json.loads(self._make_request(f'user/{user}').text)

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
        self.AUTOLOGIN = autologin
