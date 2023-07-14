template = {
    "swagger": "2.0",
    "info": {
        "title": "Student College Application",
        "description": "API for College Application",
        "contact": {
            "responsibleOrganization": "xyz",
            "responsibleDeveloper": "xyz",
            "email": "abhishah1608@gmail.com",
            "url": "xyz",
        },
        "termsOfService": "xyz",
        "version": "1.0"
    },
    "basePath": "/api/v1",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ]
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}