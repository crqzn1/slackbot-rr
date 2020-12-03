from django.db import models

# Create your models here.

class ChatChannel(models.Model):
    """
    A Slack channel logged by this application.
    """
    channel_id = models.CharField(
        unique=True,
        max_length=255,
        help_text="The id of the channel on Slack."
    )
    # slug = models.SlugField(
    #     max_length=300,
    #     unique=True,
    #     help_text="A slug for the HTML story."
    # )
    headline = models.CharField(
        max_length=255,
        help_text="Display headline for the channel."
    )
    # description = models.TextField(
    #     max_length=1000,
    #     help_text="HTML for the introductory content.",
    #     blank=True,
    # )
    # live_content = models.TextField(
    #     max_length=1000,
    #     help_text="HTML for the live content.",
    #     blank=True,
    # )

    def __str__(self):
        return self.headline


class ChatMessage(models.Model):
    """
    A Slack message posted to a channel by a user.
    """
    ts = models.CharField(
        max_length=255,
        help_text='Timestamp of the original message used by Slack as unique identifier.'
    )
    # user = models.ForeignKey(
    #     ChatUser,
    #     on_delete=models.CASCADE,
    #     help_text='Slack user the message was posted by.'
    # )
    channel = models.ForeignKey(
        ChatChannel,
        on_delete=models.CASCADE,
        help_text='Slack channel the message was posted in.'
    )
    data = models.TextField(
        max_length=255,
        help_text="The message's data"
    )
    # live = models.BooleanField(
    #     default=True,
    #     help_text='Is this message live, or was it deleted on Slack?'
    # )
    # html = models.TextField(
    #     max_length=3000,
    #     help_text='HTML code representation of the message.'
    # )
    # override_text = models.TextField(
    #     max_length=3000,
    #     blank=True,
    #     help_text="Override the message by putting text here."
    # )

    # See next section for these managers
    # objects = models.Manager()
    # messages = managers.ChatMessageManager()

    class Meta:
        ordering = ("-ts",)
        get_latest_by = "ts"

    def __str__(self):
        return self.ts