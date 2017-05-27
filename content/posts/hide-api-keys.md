Title: How to Hide Your API Keys in Python
Date: 2017-05-27 10:20
Category: tutorials
Tags:  GitHub
Slug: hide-api-keys
Authors: Monica Powell
Summary: If you plan on programming any applications and storing your code in a public GitHub repository then it is important that you protect your API keys by ensuring that they are not searchable or otherwise publicly accessible.
header_cover: images/jquery-screenshot.jpg



## Protect your application’s API Keys while committing to Git.


If you plan on programming any applications and storing your code in a public
[GitHub](https://github.com/) repository then it is important that you **protect
your API keys** 🔑 by ensuring that they are not searchable or otherwise
publicly accessible.

#### What’s an API?

An application programming interface (API) is a structured set of instructions
for building applications. If you want to leverage data from services such as
Twitter, The New York Times, [Slack](https://medium.com/@slackhq),
[Spotify](https://medium.com/@Spotify), etc. then you should read their APIs to
figure out how to structure your queries to receive data from their service or
to post on their service.

#### What are API keys?

API keys allow developers to access APIs and are unique keys associated with
that particular developer and/or application. Just like you shouldn’t share your
passwords you should **never** share your API keys. It is important to protect
your API keys so that people do not take any actions as you which could result
in your API key being revoked due to somebody else exceeding rate limits or
abusing/violating an APIs terms of service. A rate limit is when an application
limits the number of API calls that a specific application or user can make
during a specified period of time.

#### How do I protect my API keys on Github?

Here’s how to hide API keys in Python from GitHub using config.py to store your
sensitive API keys and tokens in a separate file from your main script. I used
similar code when accessing the Twitter Search API for my [blackgirlmagic
twitter bot](https://github.com/M0nica/blackgirlmagic).

#### Create 3 Files in Your Application

**config.py**

This file will store your API keys. You just need to update the portion in the
strings with your API keys, depending on the service you may or may not need all
four types of API keys. These in particular are required to create a Twitter
application.

    api_key = "YOUR_KEY"
    api_secret = "YOUR_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    token_secret = "YOUR_TOKEN_SECRET"

**main_script.py**

This file will store your main script that needs to access the API keys. This
file can be named whatever you like.

    import config
    from twython import Twython, TwythonError
    # create a Twython object by passing the necessary secret passwords
    twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)

**.gitignore**

A .gitignore file tells GitHub to ignore the noted files, directories or files
that end in specific extensions when committing files to GitHub.** This step is
crucial to ensure that your config.py file does not end up viewable on GitHub!
Here’s **[a collection of useful .gitignore
templates](https://github.com/github/gitignore)**.**

    config.py
    __pycache__
    .ipynb_checkpoints



*****

*Originally published at *[Black Tech
Diva](http://www.blacktechdiva.com/hide-api-keys/)*.
