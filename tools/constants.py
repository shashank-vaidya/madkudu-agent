from crewai.tools.base_tool import BaseTool

class EmailTool(BaseTool):
    """
    Concrete implementation of the email tool for sending emails.
    """

    def _run(self, **kwargs):
        """
        Define the behavior of the tool when executed.
        """
        # Example logic for sending an email
        recipient = kwargs.get("recipient", "unknown")
        subject = kwargs.get("subject", "No Subject")
        body = kwargs.get("body", "No Content")
        print(f"Sending email to {recipient} with subject '{subject}' and body:\n{body}")
        return "Email sent successfully."

    def __init__(self):
        super().__init__(
            name="Email Tool",
            description="A tool for creating and sending emails to leads.",
        )


def email_tool():
    """
    Returns an instance of the EmailTool class.
    """
    return EmailTool()


# Other constants (if needed)
JOB_DESCRIPTION = "Analyze lead engagement and score based on activity metrics."
