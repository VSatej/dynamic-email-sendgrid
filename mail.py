from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail # pip install sendgrid

def send_mail(name):
    """This function is used to send mail through Sendgrid API
    Args:
        data: It contains list of dictionaries with the required factories data
    Returns:
        Json Response: On success and failure
    """
    EMAIL_SENDER = ('FROM-EMAIL-ID', 'SENDER_NAME')  # account used for sending emails
    EMAIL_RECEIVERS = [('TO-EMAIL-ID', 'RECEIPENT-NAME')]
    API_CLIENT = "API_ID"
    TEMPLATE_ID = 'TEMPLATE-ID'
    try:
        message = Mail(
            from_email=EMAIL_SENDER,
            to_emails=EMAIL_RECEIVERS)
        message.template_id = TEMPLATE_ID
        if name:
            message.dynamic_template_data = {'name':name}
            sg = SendGridAPIClient(API_CLIENT)
            response = sg.send(message)
            return {'success': 'email sent', 'sendgrid': {'status_code': response.status_code}}
        else:
            message.dynamic_template_data = {'name': []}
            sg = SendGridAPIClient(API_CLIENT)
            response = sg.send(message)
            return {'success': 'email not sent', 'sendgrid': {'status_code': response.status_code}}
    except Exception as e:
        return {'error': str('mail sending: ') + str(e)}
