from framework.browser.browser import Browser


class Alert:

    @staticmethod
    def get_alert_text():
        return Browser().get_alert_text()

    @staticmethod
    def close_alert():
        Browser().accept_alert()

    @staticmethod
    def send_text(text):
        Browser().send_alert_text(text)
