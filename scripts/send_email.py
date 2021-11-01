from automator_class import Automator

IDLE_START_TIME_SEC = 3


def send_email(subject, content):
    automator = Automator()

    automator.send_email(subject, content)


if __name__ == "__main__":

    subject = "Test"
    content = "This is a test"
    send_email(subject, content)
