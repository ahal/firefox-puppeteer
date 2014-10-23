# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

class Toolbar(object):
    def __init__(self, client):
        self.client = client

    def back_button(self):
        return self.client.find_element('id', 'back-button')

    def forward_button(self):
        return self.client.find_element('id', 'forward-button')

    @property
    def location(self):
        # TODO probably doesn't work with e10s enabled
        return self.client.execute_script("""
            return gBrowser.selectedBrowser.contentWindow.location.href;
        """)

property_class = Toolbar
