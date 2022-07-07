# EPYtechIntra

## Thanks

Thanks to [norech](https://github.com/norech) for helping me build this API

## Documentation

**For all `(Json)` replies check the example section**

| Function | Definition | Description | Return value |
| -------- | ---------- | ----------- | ------------ |
| `get_payload` | `def get_payload(self) -> str:` | Returns the url base | `intra.epitech.eu/auth-XXX/` |
| `save_autologin` | `def save_autologin(self) -> None:` |Saves the current autlogin in `.intra-epitech.autologin` | `None` |
| `update_autologin` | `def update_autologin(self) -> None:` | Updates the current autologin with a new one (Also saves it with `save_autologin`) | `None` |
| `get_autologin` `by_req=True` | `def get_autologin(self, by_req: bool = False) -> str:` | Can be used to check if the given autologin works, Returns a string with the current payload | `intra.epitech.eu/auth-XXXX'` |
| `get_autologin` `by_req=False` | `def get_autologin(self, by_req: bool = False) -> str:` | Returns in a string the current autologin | `auth-XXXX` |
| `trombi` | `def trombi(self, location: List[str], prom: List[str], year: List[str], offset: int = 0) -> List[Dict(str, str)]:` | Returns the list of students matching the given parameters (All the parameters should be a list) | `(Json)` |
| `get_module` | `def get_module(self, year: str \| int, module: str, instance: str) -> Dict(str, Any):` | Returns Information about the given module | `(Json)` |
| `get_registered_module` | `def get_registered_module(self, year: str \| int, module: str, instance: str) -> List[Dict(str, Any)]:` | Returns all the users that are registered to a specific module | `(Json)` |
| `get_activity` | `def get_activity(self, year: str \| int, module: str, instance: str, activity: str) -> Dict(str, Any):` | Returns information about a specific module | `(Json)`
| `get_activity_appointments` | `def get_activity_appointments(self, year: str | int, module: str, instance: str, activity: str) -> Any:` | 

### Locations, prom aliases examples:

```python3
location = [EPYtech.EPITECH_PARIS, EPYtech.EPITECH_NICE, EPYtech.EPITECH_LA_REUNION]
# location = ['FR/PAR', 'FR/NCE', 'FR/RUN']
prom = [EPYtech.EPITECH_TEK1, EPYtech.EPITECH_TEK2, EPYtech.MSC3]
# prom = ['tek1', 'tek2', 'msc3']
year = ['2020', '2021', '2022']
```

### Trombi:

#### Request:
```python3
print(json.dumps(client.trombi([EPYtech.EPITECH_PARIS], [EPYtech.EPITECH_TEK1], ['2022']), indent=4))
```

#### Response
```json
[
    {
        "title": "John Doe",
        "login": "john.doe@epitech.eu",
        "nom": "DOE",
        "prenom": "John",
        "picture": "\/file\/userprofil\/trombiview\/john.doe@epitech.eu.jpg",
        "location": "FR\/RUN"
    },
    {
        "title": "Doe John",
        "login": "doe.john@epitech.eu",
        "nom": "JOHN",
        "prenom": "Doe",
        "picture": "\/file\/userprofil\/trombiview\/doe.john@epitech.eu.jpg",
        "location": "FR\/RUN"
    }
]
```

### Get module:

#### Request:
```python3
print(json.dumps(client.get_module(2022, EPYTech.EPITECH_PARIS, 'tek1'), indent=4))
```

#### Response:
```json
{
    "scolaryear": "XXXX",
    "codemodule": "CodeModule",
    "codeinstance": "CodeInstance",
    "semester": 1,
    "scolaryear_template": "2022",
    "title": "BX - XXXX",
    "begin": "XXXX-XX-XX",
    "end_register": "XXXX-XX-XX",
    "end": "XXXX-XX-XX",
    "past": "0",
    "closed": "0",
    "opened": "1",
    "user_credits": null,
    "credits": 0,
    "description": "Description of the unit",
    "competence": null,
    "flags": "2",
    "instance_flags": "2",
    "max_ins": null,
    "instance_location": "FR/PAR",
    "hidden": "0",
    "old_acl_backup": null,
    "resp": [],
    "assistant": [],
    "rights": null,
    "template_resp": [
        {
            "type": "user",
            "login": "john.doe@epitech.eu",
            "title": "John DOE",
            "picture": "\/file\/userprofil\/john.doe.bmp"
        },
        {
            "type": "user",
            "login": "john2.doe@epitech.eu",
            "title": "John2 Doe",
            "picture": "\/file\/userprofil\/john2.doe.bmp"
        }
    ],
    "allow_register": 1,
    "date_ins": null,
    "student_registered": 0,
    "student_grade": null,
    "student_credits": 0,
    "color": null,
    "student_flags": null,
    "current_resp": false,
    "activites": [
        {
            "codeacti": "acti-XXXXX",
            "call_ihk": "0",
            "slug": null,
            "instance_location": "FR/PAR",
            "module_title": "BX - XXXXXX",
            "title": "XXXXXXXXXX",
            "description": "XXXXX",
            "type_title": "XXXXX",
            "type_code": "class",
            "begin": "XXXX-XX-XX 00:00:00",
            "start": "XXXX-XX-XX 00:00:00",
            "end_register": null,
            "deadline": null,
            "end": "XXXX-XX-XX 00:00:00",
            "nb_hours": "00:00:00",
            "nb_group": 1,
            "num": 1,
            "register": "1",
            "register_by_bloc": "0",
            "register_prof": "0",
            "title_location_type": null,
            "is_projet": false,
            "id_projet": null,
            "project_title": null,
            "is_note": false,
            "nb_notes": null,
            "is_blocins": false,
            "rdv_status": "close",
            "id_bareme": null,
            "title_bareme": null,
            "archive": "1",
            "hash_elearning": null,
            "ged_node_adm": null,
            "nb_planified": 1,
            "hidden": false,
            "project": null,
            "events": [
                {
                    "code": "event-XXXXX",
                    "num_event": "1",
                    "seats": "100",
                    "title": null,
                    "description": null,
                    "nb_inscrits": "125",
                    "begin": "XXXX-XX-XX 00:00:00",
                    "end": "XXXX-XX-XX 00:00:00",
                    "id_activite": "521505",
                    "location": "FR/PAR/LocationName",
                    "nb_max_students_projet": null,
                    "already_register": null,
                    "user_status": null,
                    "allow_token": "1",
                    "assistants": [
                        {
                            "login": "asssitant.one@epitech.eu",
                            "title": "Assistant ONE",
                            "picture": "assistant.one@epitech.eu.bmp",
                            "manager_status": "accept"
                        }
                    ]
                }
            ]
        }
    ]
}
```

### Get registered module

#### Request:

```python3
print(json.dumps(client.get_registered_module(2022, EPYTech.EPITECH_PARIS, 'tek1'), indent=4))
```

#### Response:

```json
[
    {
        "login": "john.doe@epitech.eu",
        "picture": "\/file\/userprofil\/john.doe@epitech.eu.bmp",
        "title": "John DOE",
        "location": null,
        "promo": 2022,
        "course_code": "XXXXXXx",
        "grade": null,
        "cycle": "XXXXX",
        "date_ins": "XXXX-XX-XX 00:00:00",
        "credits": 0,
        "flags": [],
        "semester": "XX"
    }
]
```

### Get activity:

#### Request:
```python3
print(json.dumps(client.get_activity(2022, 'XXXX', 'XXXX', 'XXXX'), indent=4))
```

#### Response:
```json
{
    "scolaryear": "2022",
    "codemodule": "X-XXX-XXX",
    "codeinstance": "XXX-X-X",
    "codeacti": "acti-XXXXXX",
    "call_ihk": "1",
    "slug": "name",
    "instance_location": "FR\/PAR",
    "module_title": "XX - XXXXXXX",
    "title": "XXXXXXXX",
    "description": "",
    "type_title": "XXXXXX",
    "type_code": "proj",
    "begin": "0000-00-00 00:00:00",
    "start": "0000-00-00 00:00:00",
    "end_register": "0000-00-00 00:00:00",
    "deadline": null,
    "end": "0000-00-00 00:00:00",
    "nb_hours": null,
    "nb_group": 1,
    "num": 1,
    "register": "0",
    "register_by_bloc": "0",
    "register_prof": "0",
    "title_location_type": null,
    "is_projet": true,
    "id_projet": "0",
    "project_title": "XXXXX",
    "is_note": true,
    "nb_notes": 0,
    "is_blocins": false,
    "rdv_status": "close",
    "id_bareme": null,
    "title_bareme": null,
    "archive": "1",
    "hash_elearning": null,
    "ged_node_adm": null,
    "nb_planified": null,
    "hidden": false,
    "project": null,
    "student_registered": null,
    "events": []
}
```

### Get activity appointments:

#### Request:
```python3
print(json.dumps(client.get_activity_appointments(2022, 'XXXX', 'XXXX', 'XXXX'), indent=4))
```

#### Response:

```json
{
    "scolaryear": "XXXX",
    "codemodule": "X-XXX-XXX",
    "codeinstance": "XXX",
    "codeacti": "acti-XXXXX",
    "nb_notes": 0,
    "register_by_bloc": false,
    "group": {
        "id": 15097109357,
        "code": "XXXXX",
        "title": "XXXXX",
        "inscrit": true,
        "master": "john.doe@epitech.eu",
        "members": [
            "john2.doe@epitech.eu"
        ]
    },
    "projects": [
        {
            "title": "Follow-up - XXXX",
            "codeacti": "acti-XXXXXX",
            "id_projet": null
        }
    ],
    "events": [
        {
            "id": "XXXXXX",
            "nb_registered": "0",
            "begin": "XXXX-XX-XX 00:00:00",
            "register": "0",
            "num_event": "1",
            "end": "XXXX-XX-XX 00:00:00",
            "location": "XXXXXX",
            "title": "Follow-up - XXXX",
            "date_ins": null,
            "date_modif": null
        }
    ],
    "title": "Follow-up - XXXXXX",
    "description": "",
    "instance_location": "XXXXX",
    "module_title": "BX - XXXXXXXXXXXX",
    "project": {
        "id": 15097109357,
        "scolaryear": "2021",
        "codemodule": "X-XXXX-XXX",
        "codeinstance": "XXXX-X-X",
        "title": "XXXXXXXXXXX"
    },
    "student_registered": true,
    "with_project": true,
    "nb_registered": 24,
    "nb_slots_full": 10,
    "slots": [
        {
            "id": 156046,
            "title": "",
            "bloc_status": "oneshot",
            "room": "XXXXXXXXX",
            "slots": [
                {
                    "acti_title": "Follow-up - XXXXX",
                    "date": "XXXX-XX-XX 00:00:00",
                    "duration": 60,
                    "status": "open",
                    "bloc_status": "oneshot",
                    "id_team": null,
                    "id_user": null,
                    "date_ins": null,
                    "code": null,
                    "title": null,
                    "module_title": "XX - XXXXX",
                    "members_pictures": null,
                    "past": 1,
                    "master": null,
                    "members": [],
                    "id": 1884195
                }
            ],
            "codeevent": "event-XXXXXXX"
        }
    ]
}
