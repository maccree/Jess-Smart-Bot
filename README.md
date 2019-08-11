**For the bot to work:**


***
1. Install libraries: Telegram.ext, PyTelegram, apiai.

***

```bash
pip install python-telegram-bot --upgrade
```

***

```bash
pip install telegram --upgrade
```

***

```bash
pip install apiai --upgrade
```


***

2. Create file __token_for_bot.py__

(The file should be with the following contents)

```python
token_for_bot = '<ur token>'
```

***

3. Register on [Dialogflow](https://console.dialogflow.com). Click on the __Create__ agent button and fill in the fields as you wish. 
Click on __Prebuilt Agents__ and select __Small Talk__.
Point to it and click __Import__. Further, without changing anything, click __Ok__. The agent was imported and now we can configure it. To do this, in the upper left corner, click on the __gear near Small-Talk__ and get to the settings page.
Change the time zone in the __Languages tab__.
Go back to the __General tab__, go down a bit and __copy Client access token__. And insert __Client access token__ into the __token_for_dialogflow.py__ file


***

4. Create file __token_for_dialogflow.py__

(The file should be with the following contents)

```python
token_for_dialogflow = '<ur Client access token>'
```

***

**You can engage in bot training in the TRAINING TAB**
