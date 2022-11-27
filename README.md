# event_bot

event_bot works as a Discord bot written in Python 3, and can be deployed using AWS + SAM.

event_bot runs a cron job daily that posts to a Discord channel about birthdays and anniversaries. It posts the day of and 2 days before specified events.

## Prerequisites
1. A [webhook URL for your Discord channel](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
2. An AWS account [with an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
3. [AWS CLI installed and configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
4. [AWS SAM CLI installed and configured](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
5. [Docker installed and configured](https://docs.docker.com/get-docker/)

## Setup

1. Add your webhook URL into [the webhook variable in app.py](https://github.com/thaigoonch/event_bot/blob/main/app.py#L72)
2. Modify the [birthday/anniversary dates in app.py](https://github.com/thaigoonch/event_bot/blob/main/app.py#L9-L16) as desired.
3. Modify the [schedule time in template.yaml](https://github.com/thaigoonch/event_bot/blob/main/template.yaml#L16) to the desired time (in UTC). The syntax for AWS crons can be found [here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html).
4. Run:
``` bash
sam build --use-container
```
5. Run:
``` bash
sam deploy --guided
```
6. To test (recommended to do using the webhook for a test discord channel), run:
```bash
aws lambda invoke --function-name EVENT_BOT output.txt
```

Expected output: 
``` bash
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```
Expected contents of `output.txt`:
``` bash
null
```
After testing, re-run steps 4 & 5 after changing the webhook URL/cron time to the desired values.

### Additional Resources
For more details, reference [this blog](https://levelup.gitconnected.com/deploy-a-python-cron-job-to-aws-lambda-with-sam-5d05f0c17a89).