# EPYtechIntra

## Thanks

Thanks to [norech](https://github.com/norech) for helping me build this API

## Documentation

| Function | Description | Return value |
| -------- | ----------- | ------------ |
| `get_payload` | Returns the url base | `intra.epitech.eu/auth-XXX/` |
| `save_autologin` | Saves the current autlogin in `.intra-epitech.autologin` | `None` |
| `update_autologin` | Updates the current autologin with a new one (Also saves it with `save_autologin`) | `None` |
| `get_autologin` `by_req=True` | Can be used to check if the given autologin works, Returns a string with the current payload | `intra.epitech.eu/auth-XXXX'` |
| `get_autologin` `by_req=False` | Returns in a string the current autologin | `auth-XXXX` |
| `trombi` | Returns the list of students matching the given parameters (All the parameters should be a list) | `(Json) See Trombi example` |
| `get_module` |

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
print(json.dumps(client.trombi([EPYTech.EPITECH_PARIS], ['tek1', 'tek2'], ['XXXX']), indent=4))
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
