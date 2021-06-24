{
  "id": "4f85410b-87d6-4fda-9ad0-1b81031f2712",
  "version": "2.0",
  "name": "http://selenium1py.pythonanywhere.com/ru/accounts/login/",
  "url": "http://selenium1py.pythonanywhere.com",
  "tests": [{
    "id": "bdba2ee1-c9d0-426a-9339-186bd6d735dc",
    "name": "Untitled",
    "commands": [{
      "id": "a80351ba-5d31-4f46-9902-246bad579ffe",
      "comment": "",
      "command": "open",
      "target": "/ru/accounts/login/",
      "targets": [],
      "value": ""
    }, {
      "id": "74d029d2-d042-42be-bafb-17aef941fd6c",
      "comment": "",
      "command": "setWindowSize",
      "target": "1478x824",
      "targets": [],
      "value": ""
    }, {
      "id": "772d9aec-a335-4742-9cc8-054cc54df43d",
      "comment": "",
      "command": "click",
      "target": "id=id_registration-email",
      "targets": [
        ["id=id_registration-email", "id"],
        ["name=registration-email", "name"],
        ["css=#id_registration-email", "css:finder"],
        ["xpath=//input[@id='id_registration-email']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "dd550ddc-5a76-4389-958d-340a89a3ef97",
      "comment": "",
      "command": "mouseDownAt",
      "target": "id=login_form",
      "targets": [
        ["id=login_form", "id"],
        ["css=#login_form", "css:finder"],
        ["xpath=//form[@id='login_form']", "xpath:attributes"],
        ["xpath=//div[@id='content_inner']/div/div/form", "xpath:idRelative"],
        ["xpath=//div[2]/div[2]/div/div/form", "xpath:position"]
      ],
      "value": "554.8000030517578,134.60000610351562"
    }, {
      "id": "06cb7b99-f210-4cb1-8f12-4037ae09ae21",
      "comment": "",
      "command": "mouseMoveAt",
      "target": "id=login_form",
      "targets": [
        ["id=login_form", "id"],
        ["css=#login_form", "css:finder"],
        ["xpath=//form[@id='login_form']", "xpath:attributes"],
        ["xpath=//div[@id='content_inner']/div/div/form", "xpath:idRelative"],
        ["xpath=//div[2]/div[2]/div/div/form", "xpath:position"]
      ],
      "value": "554.8000030517578,134.60000610351562"
    }, {
      "id": "1496a2dc-f6f3-404f-8871-43a10cc481b8",
      "comment": "",
      "command": "mouseUpAt",
      "target": "id=login_form",
      "targets": [
        ["id=login_form", "id"],
        ["css=#login_form", "css:finder"],
        ["xpath=//form[@id='login_form']", "xpath:attributes"],
        ["xpath=//div[@id='content_inner']/div/div/form", "xpath:idRelative"],
        ["xpath=//div[2]/div[2]/div/div/form", "xpath:position"]
      ],
      "value": "554.8000030517578,134.60000610351562"
    }, {
      "id": "f787baa0-fd76-4229-910b-a231a3af5da9",
      "comment": "",
      "command": "click",
      "target": "css=#content_inner > .row",
      "targets": [
        ["css=#content_inner > .row", "css:finder"],
        ["xpath=//div[@id='content_inner']/div", "xpath:idRelative"],
        ["xpath=//div[2]/div[2]/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5e460e45-eaba-42c1-bb0c-17a703ef3420",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-email",
      "targets": [
        ["id=id_registration-email", "id"],
        ["name=registration-email", "name"],
        ["css=#id_registration-email", "css:finder"],
        ["xpath=//input[@id='id_registration-email']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div/div/input", "xpath:position"]
      ],
      "value": "gg5gjcgcf@ggg.hh"
    }, {
      "id": "9b3f2f34-c1ce-45f2-ae74-0f4d7fbb7b47",
      "comment": "",
      "command": "click",
      "target": "id=id_registration-password1",
      "targets": [
        ["id=id_registration-password1", "id"],
        ["name=registration-password1", "name"],
        ["css=#id_registration-password1", "css:finder"],
        ["xpath=//input[@id='id_registration-password1']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ed5e38e7-d21a-4754-a43e-8f6e9de7e60b",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-password1",
      "targets": [
        ["id=id_registration-password1", "id"],
        ["name=registration-password1", "name"],
        ["css=#id_registration-password1", "css:finder"],
        ["xpath=//input[@id='id_registration-password1']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div[2]/div/input", "xpath:position"]
      ],
      "value": "gg5gjcgcf@ggg.hh"
    }, {
      "id": "58a83ada-2c86-4a5e-a82b-661c21fcb8f0",
      "comment": "",
      "command": "click",
      "target": "id=id_registration-password2",
      "targets": [
        ["id=id_registration-password2", "id"],
        ["name=registration-password2", "name"],
        ["css=#id_registration-password2", "css:finder"],
        ["xpath=//input[@id='id_registration-password2']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[3]/div/input", "xpath:idRelative"],
        ["xpath=//div[3]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d80cb8cc-1ebc-4e1b-85f8-cefd7b25a1c1",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-password2",
      "targets": [
        ["id=id_registration-password2", "id"],
        ["name=registration-password2", "name"],
        ["css=#id_registration-password2", "css:finder"],
        ["xpath=//input[@id='id_registration-password2']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[3]/div/input", "xpath:idRelative"],
        ["xpath=//div[3]/div/input", "xpath:position"]
      ],
      "value": "gg5gjcgcf@ggg.hh"
    }, {
      "id": "959e0bf3-874c-4cba-8416-2c045e82d2dc",
      "comment": "",
      "command": "click",
      "target": "name=registration_submit",
      "targets": [
        ["name=registration_submit", "name"],
        ["css=#register_form > .btn", "css:finder"],
        ["xpath=//button[@name='registration_submit']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/button", "xpath:idRelative"],
        ["xpath=//div[2]/form/button", "xpath:position"],
        ["xpath=//button[contains(.,'Зарегистрироваться')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "142a0dd3-dc56-44e3-b28a-db107068e0c3",
      "comment": "",
      "command": "click",
      "target": "css=.alertinner",
      "targets": [
        ["css=.alertinner", "css:finder"],
        ["xpath=//div[@id='messages']/div/div", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/div/div/div/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4650397d-5bb0-4b90-81d7-2dbd69c38fa2",
      "comment": "",
      "command": "click",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "753156d9-d930-4e0e-ba14-d200d7caf413",
      "comment": "",
      "command": "click",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "cd505e40-e70f-4158-9c92-353a52ba1ebd",
      "comment": "",
      "command": "click",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "017672ce-1677-4a52-a9cc-096094586c16",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["bdba2ee1-c9d0-426a-9339-186bd6d735dc"]
  }],
  "urls": ["http://selenium1py.pythonanywhere.com/"],
  "plugins": []
}