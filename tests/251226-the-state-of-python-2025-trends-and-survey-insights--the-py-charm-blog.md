# The State of Python 2025: Trends and Survey Insights | The PyCharm Blog

## The State of Python 2025: Trends and Survey Insights

Read this post in other languages:

- [Deutsch](https://blog.jetbrains.com/de/pycharm/2025/09/wo-steht-python-im-jahr-2025/)
,- [Español](https://blog.jetbrains.com/es/pycharm/2025/09/el-estado-de-python-2025/)
,- [Français](https://blog.jetbrains.com/fr/pycharm/2025/09/l-etat-de-python-en-2025/)
,- [日本語](https://blog.jetbrains.com/ja/pycharm/2025/09/the-state-of-python/)
,- [한국어](https://blog.jetbrains.com/ko/pycharm/2025/09/the-state-of-python-2025/)
,- [简体中文](https://blog.jetbrains.com/zh-hans/pycharm/2025/09/the-state-of-python-2025/)
,- [Português do Brasil](https://blog.jetbrains.com/pt-br/pycharm/2025/09/o-estado-do-python-em-2025/)

*This is a guest post from , the founder of Talk Python and a PSF Fellow.*

![State of Python 2025](https://blog.jetbrains.com/wp-content/uploads/2025/08/Blog-Featured-1280x720-1-2.png)

State of Python 2025

Welcome to the highlights, trends, and key actions from the [eighth annual Python Developers Survey](https://lp.jetbrains.com/python-developers-survey-2024/). This survey is conducted as a collaborative effort between the Python Software Foundation and JetBrains’ PyCharm team. The survey results provide a comprehensive look at Python usage statistics and popularity trends in 2025.

My name is Michael Kennedy, and I’ve analyzed the more than 30,000 responses to the survey and pulled out the most significant trends and predictions, and identified various actions that you can take to improve your Python career.

I am in a unique position as the host of the *Talk Python to Me* podcast. Every week for the past 10 years, I’ve interviewed the people behind some of the most important libraries and language trends in the Python ecosystem. In this article, my goal is to use that larger community experience to understand the results of this important yearly survey.

If your job or products and services depend on Python, or developers more broadly, you’ll want to read this article. It provides a lot of insight that is difficult to gain from other sources.

Let’s dive into the most important trends based on the Python survey results.

![Infographic showing key Python trends in 2025](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-14.png)

Infographic showing key Python trends in 2025

As you explore these insights, having the right tools for your projects can make all the difference. Try PyCharm for free and stay equipped with everything you need for data science, ML/AI workflows, and web development in one powerful Python IDE.

[Try PyCharm for free](https://www.jetbrains.com/pycharm/download/)

Let’s begin by talking about how central Python is for people who use it. Python people use Python primarily. That might sound like an obvious tautology. However, developers use many languages that are not their primary language. For example, web developers might use Python, C#, or Java primarily, but they also use CSS, HTML, and even JavaScript.

On the other hand, developers who work primarily with Node.js or Deno also use JavaScript, but not as their primary language.

⁠⁠ The survey shows that **86% of respondents use Python as their main language** for writing computer programs, building applications, creating APIs, and more.⁠⁠

![Donut chart of Python usage in 2025: 86% use Python as main language, 14% as secondary.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-15.png)

Donut chart of Python usage in 2025: 86% use Python as main language, 14% as secondary.

For those of us who have been programming for a long time – I include myself in this category, having written code for almost 30 years now – it’s easy to imagine that most people in the industry have a decent amount of experience. It’s a perfectly reasonable assumption. You go to conferences and talk with folks who have been doing programming for 10 or 20 years. You look at your colleagues, and many of them have been using Python and programming for a long time.

But that is not how the broader Python ecosystem looks.

Exactly 50% of respondents have less than two years of professional coding experience! And 39% have less than two years of experience with Python (even in hobbyist or educational settings).

![Bar chart of developers’ coding experience: 31% less than 1 year, 19% with 1–2 years, 20% with 3–5 years, 13% with 6–10 years, 17% with 11+ years.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-16.png)

Bar chart of developers’ coding experience: 31% less than 1 year, 19% with 1–2 years, 20% with 3–5 years, 13% with 6–10 years, 17% with 11+ years.

This result reaffirms that Python is a great language for those early in their career. The simple (but not simplistic) syntax and approachability really speak to newer programmers as well as seasoned ones. Many of us love programming and Python and are happy to share it with our newer community members.

However, it suggests that we consider these demographics when we create content for the community. If you create a tutorial or video demonstration, don’t skimp on the steps to help people get started. For example, don’t just tell them to install the package. Tell them that they need to [create a virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html), and show them how to do so and how to activate it. Guide them on installing the package into that virtual environment.

If you’re a tool vendor such as JetBrains, you’ll certainly want to keep in mind that many of your users will be quite new to programming and to Python itself. That doesn’t mean you should ignore advanced features or dumb down your products, but don’t make it hard for beginners to adopt them either.

⁠⁠ This year, 51% of all surveyed Python developers are involved in [data exploration and processing](https://www.jetbrains.com/pycharm/data-science/), with pandas and NumPy being the tools most commonly used for this.⁠⁠

Many of us in the Python pundit space have talked about Python as being divided into thirds: One-third web development, one-third [Python for data science](https://www.jetbrains.com/pycharm/data-science/) and pure science, and one-third as a catch-all bin.

We need to rethink that positioning now that one of those thirds is overwhelmingly the most significant portion of Python.

This is also in the context of not only a massive boom in the interest in data and AI right now, but a corresponding explosion in the development of tools to work with in this space. There are data processing tools like Polars, new ways of working with notebooks like Marimo, and a huge number of user friendly packages for working with LLMs, vision models, and agents, such as Transformers (the Hugging Face library for LLMs), Diffusers (for diffusion models), smolagents, LangChain/LangGraph (frameworks for LLM agents) and LlamaIndex (for indexing knowledge for LLMs).

**⁠⁠ Python’s center of gravity has indeed tilted further toward data/AI**.⁠⁠

⁠⁠ The survey shows a distribution across the latest and older versions of the Python runtime. Many of us (15%) are running on the very latest released version of Python, but **more likely than not, we’re using a version a year old or older (83%)**.⁠⁠

![Bar chart of Python version usage in 2025: 35% on Python 3.12, 21% on 3.11, 15% on 3.13, smaller shares on older versions.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-17.png)

Bar chart of Python version usage in 2025: 35% on Python 3.12, 21% on 3.11, 15% on 3.13, smaller shares on older versions.

⁠⁠ The survey also indicates that many of us are using Docker and containers to execute our code, which makes this 83% or higher number even more surprising ⁠⁠. With containers, just pick the latest version of Python in the container. Since everything is isolated, you don’t need to worry about its interactions with the rest of the system, for example, Linux’s system Python. We should expect containerization to provide more flexibility and ease our transition towards the latest version of Python.

So why haven’t people updated to the latest version of Python? The survey results give two primary reasons.

1. The version I’m using meets all my needs (53%)
2. I haven’t had the time to update (25%)

⁠⁠ The 83% of developers running on older versions of Python may be missing out on much more than they realize. It’s not just that they are missing some language features, such as the `except` keyword, or a minor improvement to the standard library, such as `tomllib`. **Python 3.11, 3.12, and 3.13 all include major performance benefits**, and the upcoming 3.14 will include even more.⁠⁠

⁠⁠ What’s amazing is you get these benefits without changing your code. You simply choose a newer runtime, and your code runs faster. CPython has been extremely good at backward compatibility. There’s rarely significant effort involved in upgrading.⁠⁠ Let’s look at some numbers.

**⁠⁠ 48% of people are currently using Python 3.11.** Upgrading to 3.13 will make their code run ~ **11% faster** end to end while using ~ **10-15% less memory**.⁠⁠

⁠⁠ If they are one of the 27% still on **3.10 or older**, their code gets **a whopping ~42% speed increase** (with no code changes), and **memory use can drop by ~20-30%**!⁠⁠

⁠⁠ So maybe they’ll still come back to “Well, it’s fast enough for us. We don’t have that much traffic, etc.”. But if they are like most medium to large businesses, this is an incredible waste of cloud compute expense (which also maps to environmental harm via spent energy).⁠⁠

⁠⁠ Research shows some estimates for cloud compute ⁠⁠ (specifically computationally based):

- **Mid-market / “medium” business**
	- Total annual AWS bill (median): ~ $2.3 million per year ([vendr.com](https://www.vendr.com/marketplace/aws))
	- EC2 (compute-instance) share (~ 50–70 % of that bill): $1.15–1.6 million per year ([cloudlaya.com](https://www.cloudlaya.com/blog/the-real-cost-of-ec2-instance/))
- **Large enterprise**
	- Total annual AWS bill: ~ $24–36 million per year (i.e. $2–3 million per month) ([reddit.com](https://www.reddit.com/r/aws/comments/1b6r50v/ballpark_how_much_is_your_total_spend_on_aws/))
	- EC2 share (~ 50–70 %): $12–25 million per year ([cloudlaya.com](https://www.cloudlaya.com/blog/the-real-cost-of-ec2-instance/))

⁠⁠ If we assume they’re running Python 3.10, that’s potentially **$420,000** and **$5.6M in savings**, respectively (computed as 30% of the EC2 cost).⁠⁠

⁠⁠ If your company realizes you are burning an extra $0.4M-$5M a year because you haven’t gotten around to spending the day it takes to upgrade, that’ll be a tough conversation.⁠⁠

⁠⁠ Finances and environment aside, it’s really great to be able to embrace the latest language features and be in lock-step with the core devs’ significant work. **Make upgrading a priority**,folks.⁠⁠

⁠⁠ For the past few years, we’ve heard that the significance of web development within the Python space is decreasing. Two powerful forces could be at play here: 1) As more data science and AI-focused people come to Python, the relatively static number of web devs represents a lower percentage, and 2) The web continues to be frontend-focused, and until Python in the browser becomes a working reality, web developers are likely to prefer JavaScript.⁠⁠

⁠⁠ Looking at the numbers from 2021–2023, the trend is clearly downward 45% → 43% → 42%. **But this year, the web is back**! Respondents reported that 46% of them are using Python for web development in 2024. To bolster this hypothesis further, we saw web “secondary” languages jump correspondingly, with HTML/CSS usage up 15%, JavaScript usage up 14%, and SQL’s usage up 16%.⁠⁠

![Line chart of Python use cases 2021–2024: data analysis at 48%, web development at 46%, machine learning at 41% in 2024.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-18.png)

Line chart of Python use cases 2021–2024: data analysis at 48%, web development at 46%, machine learning at 41% in 2024.

⁠⁠ The biggest winner of the Python web frameworks was FastAPI, which jumped from 29% to 38% (a 30% increase).⁠⁠ ⁠⁠ While all of the major frameworks grew year over year, FastAPI’s nearly 30% jump is impressive. I can only speculate why this is. To me, I think this jump in Python for web is likely partially due to a large number of newcomers to the Python space.⁠⁠ ⁠⁠ Many of these are on the ML/AI/data science side of things, and those folks often don’t have years of baked-in experience and history with Flask or Django ⁠⁠. They are likely choosing the hottest of the Python web frameworks, which today looks like it’s FastAPI. ⁠⁠ There are many examples of people hosting their ML models behind FastAPI APIs.⁠⁠

![Line chart of Python web frameworks 2021–2024: FastAPI rose to 38%, Django declined to 35%, Flask declined to 34%.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-19.png)

Line chart of Python web frameworks 2021–2024: FastAPI rose to 38%, Django declined to 35%, Flask declined to 34%.

The trend towards async-friendly Python web frameworks has been continuing as well. Over at *Talk Python*, I [rewrote our Python web app in async Flask](https://talkpython.fm/blog/posts/talk-python-rewritten-in-quart-async-flask/) (roughly 10,000 lines of Python). Django has been steadily adding async features, and its async support is nearly complete. Though today, at version 5.2, its DB layer needs a bit more work, as the team says: “We’re still working on async support for the ORM and other parts of Django.”

⁠⁠ It’s worth a brief mention that the production app servers hosting Python web apps and APIs are changing too.⁠⁠ Anecdotally, I see two forces at play here: ⁠⁠ 1) The move to async frameworks necessitates app servers that support [ASGI](https://asgi.readthedocs.io/en/latest/specs/main.html), not just [WSGI ⁠⁠](https://peps.python.org/pep-3333/) and ⁠⁠ 2) Rust is becoming more and more central to the fast execution of Python code (we’ll dive into that shortly) ⁠⁠.

⁠⁠ The biggest loss in this space last year was the complete demise of uWSGI. We even did a *Python Bytes* podcast entitled *We Must Replace uWSGI With Something Else* examining this situation in detail.⁠⁠

⁠⁠ We also saw Gunicorn handling less of the async workload with async-native servers such as [uvicorn](https://www.uvicorn.org/) and [Hypercorn](https://github.com/pgjones/hypercorn), which are able to [operate independently](https://github.com/encode/uvicorn/pull/2183). Newcomer servers, based on Rust, such as [Granian](https://github.com/emmett-framework/granian), have gained a solid following as well.⁠⁠

⁠⁠ Over the past couple of years, Rust has become Python’s performance co-pilot. The Python Language Summit of 2025 [revealed](https://pyfound.blogspot.com/2025/06/python-language-summit-2025-what-do-core-developers-want-from-rust.html) that “Somewhere between one-quarter and one-third of all native code being uploaded to PyPI for new projects uses Rust”, indicating that “people are choosing to start new projects using Rust”.⁠⁠

Looking into the survey results, we see that ⁠⁠ Rust usage grew from 27% to 33% for binary extensions to Python packages.⁠⁠ This reflects a growing trend toward using Rust for systems-level programming and for native extensions that accelerate Python code.

![Bar chart comparing 2023 vs 2024: 55% use C++, 45% use C, 33% use Rust for Python binary modules.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-20.png)

Bar chart comparing 2023 vs 2024: 55% use C++, 45% use C, 33% use Rust for Python binary modules.

⁠⁠ We see this in the ecosystem with the success of Polars for data science and Pydantic for pretty much all disciplines.⁠⁠ ⁠⁠ We are even seeing that for Python app servers such as the newer Granian.⁠⁠

Another key trend this year is static type checking in Python. You’ve probably seen Python type information in function definitions such as:

`⁠⁠def add(x: int, y: int) -> int: ...⁠⁠ `

These have been in Python for a while now. Yet, there is a renewed effort to make typed Python more common and more forgiving. ⁠⁠ We’ve had tools such as mypy since typing’s early days, but the goal there was more along the lines of whole program consistency. In just the past few months, we have seen two new high-performance typing tools released:⁠⁠

- [⁠⁠ ty](https://github.com/astral-sh/ty) from Astral – an extremely fast Python type checker and language server written in Rust.⁠⁠
- [⁠⁠ Pyrefly](https://pyrefly.org/) from Meta – a faster Python type checker written in Rust.⁠⁠

ty and Pyrefly provide extremely fast static type checking and language server protocols (LSPs). These next‑generation type checkers make it easier for developers to adopt type hints and enforce code quality.

⁠⁠ Notice anything similar? They are both written in Rust, backing up the previous claim that “Rust has become Python’s performance co-pilot”.⁠⁠

By the way, [I interviewed the team](https://talkpython.fm/episodes/show/506/ty-astrals-new-type-checker-formerly-red-knot) behind ty when it was announced a few weeks ago if you want to dive deeper into that project.

There are many different and unique ways to contribute to open source. Probably the first thing that comes to most people’s minds when they think of a contributor is someone who writes code and adds a new feature to that project. However, there are less visible but important ways to make a contribution, such as triaging issues and reviewing pull requests.

So, what portion of the community has contributed to open source, and in which ways have they done so?

The survey tells us that one-third of devs contributed to open source. This manifests primarily as code and documentation/tutorial additions.

![Bar chart of open-source contributions in 2025: 78% code, 40% documentation, 35% governance, 33% tests.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-21.png)

Bar chart of open-source contributions in 2025: 78% code, 40% documentation, 35% governance, 33% tests.

Where do you typically learn as a developer or data scientist? Respondents said that docs are #1. There are many ways to learn languages and libraries, but people like docs best. This is good news for open-source maintainers. This means that the effort put into documentation (and embedded tutorials) is well spent. It’s a clear and straightforward way to improve users’ experience with your project.

Moreover, this lines up with [*Developer Trends in 2025*](https://talkpython.fm/episodes/show/504/developer-trends-in-2025), a podcast panel episode I did with experienced Python developers, including JetBrains’ own Paul Everitt. The panelists all agree that docs are #1, though the survey ranked YouTube much higher than the panelists, at 51%. Remember, our community has an average of 1–2 years of experience, and 45% of them are younger than 30 years old.

Respondents said that documentation and embedded tutorials are the top learning resources. Other sources, such as YouTube tutorials, online courses, and AI-based code generation tools, are also gaining popularity. In fact, the survey shows that AI tools as a learning source increased from 19 % to 27 % (up 42% year over year)!

When asked which database (if any) respondents chose, they overwhelmingly said PostgreSQL. This relational database management system (RDBMS) grew from 43 % to 49 %. That’s +14% year over year, which is remarkable for a 28-year-old open-source project.

![Bar chart of databases used in 2023 vs 2024: PostgreSQL grew to 49%, SQLite 37%, MySQL 31%.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-22.png)

Bar chart of databases used in 2023 vs 2024: PostgreSQL grew to 49%, SQLite 37%, MySQL 31%.

One interesting detail here, beyond Postgres being used a lot, is that every single database in the top six, including MySQL and SQLite, grew in usage year over year. This is likely another indicator that web development itself is growing again, as discussed above.

My first forward-looking trend is that agentic AI will be a game-changer for coding. Agentic AI is often cited as a tool of the much maligned and loved [vibe coding](https://www.youtube.com/watch?v=_2C2CNmK7dQ). However, **vibe coding obscures the fact that agentic AI tools are remarkably productive when used alongside a talented engineer or data scientist**.

Surveys outside the PSF survey indicate that about 70% of developers were using or planning to use AI coding tools in 2023, and by 2024, around 44% of professional developers use them daily.

JetBrains’ *State of Developer Ecosystem 2023* report noted that within a couple of years, “AI-based code generation tools went from interesting research to an important part of many developers’ toolboxes”. Jump ahead to 2025, according to the *State of Developer Ecosystem 2025* survey, **nearly half of the respondents (49%) plan to try AI coding agents in the coming year**.

![Bar chart showing adoption of AI coding agents in 2025: 49% very likely, 20% somewhat likely, 11% already using.](https://blog.jetbrains.com/wp-content/uploads/2025/08/image-23.png)

Bar chart showing adoption of AI coding agents in 2025: 49% very likely, 20% somewhat likely, 11% already using.

Program managers at major tech companies have stated that they almost cannot hire developers who don’t embrace agentic AI. The productive delta between those using it and those who avoid it is simply too great (estimated at about 30% greater productivity with AI).

⁠⁠ The future will be abuzz with concurrency and Python. We’ve already discussed how the Python web frameworks and app servers are all moving towards asynchronous execution, but this only represents one part of a powerful trend.⁠⁠

⁠⁠ Python 3.14 will be the first version of Python to completely support free-threaded Python. Free-threaded Python, which is a version of the Python runtime that does not use the GIL, the global interpreter lock, was first added as an experiment to CPython 3.13.⁠⁠

Just last week, the ⁠⁠ steering council and core developers officially accepted this as a permanent part of the language and runtime. This will have far-reaching effects. Developers and data scientists will have to think more carefully about threaded code with locks, race conditions, and the performance benefits that come with it.⁠⁠ Package maintainers, especially those with native code extensions, may have to rewrite some of their code to support free-threaded Python so they themselves do not enter race conditions and deadlocks.

⁠⁠ There is a massive upside to this as well. I’m currently writing this on the cheapest Apple Mac Mini M4. This computer comes with 10 CPU cores.⁠⁠ That means until this change manifests in Python, the ⁠⁠ maximum performance I can get out of a single Python process is 10% of what my machine is actually capable of.⁠⁠ ⁠⁠ Once free-threaded Python is fully part of the ecosystem, I should get much closer to maximum capacity with a standard Python program using threading and the async and await keywords.⁠⁠

`Async` and `await` keywords are not just tools for web developers who want to write more concurrent code. It’s appearing in more and more locations. One such ⁠⁠ tool that I recently came across is [Temporal](https://temporal.io/).⁠⁠ This program leverages the asyncio event loop but replaces the standard clever threading tricks with durable machine-spanning execution. You might simply await some action, and behind the scenes, you ⁠⁠ get durable execution that survives machine restarts.⁠⁠ So ⁠⁠ understanding `async` and `await` is going to be increasingly important as more tools make interesting use of it, as Temporal did.⁠⁠

I see parallels here of how ⁠⁠ Pydantic made a lot of people more interested in Python typing than they otherwise would have been.⁠⁠

My last forward-looking trend is that Python GUIs and Python on mobile are rising. When we think of native apps on iOS and Android, we can only dream of using Python to build them someday soon.

At the 2025 Python Language Summit, Russell Keith-Magee presented his work on making iOS and Android Tier 3-supported platforms for CPython. This has been laid out in PEP 730 and PEP 738. This is a necessary but not sufficient condition for allowing us to write true native apps that ship to the app stores using Python.

More generally, there have been some interesting ideas and new takes on UIs for Python. We had Jeremy Howard from fast.ai introduce [FastHTML](https://www.fastht.ml/), which allows us to write modern web applications in pure Python. [NiceGUI](https://nicegui.io/) has been coming on strong as an excellent way to write web apps and PWAs in pure Python.

I expect these changes, especially the mobile ones, to unlock powerful use cases that we’ll be talking about for years to come.

You’ve seen the results, my interpretations, and predictions. So what should you do about them? Of course, nothing is required of you, but I am closing out this article with some actionable ideas to help you take advantage of these technological and open-source waves.

⁠⁠ Here are six actionable ideas you can put into practice after reading this article.⁠⁠ Pick your favorite one that you’re not yet leveraging and see if it can help you thrive further in the Python space.

[⁠⁠ uv](https://astral.sh/uv/), the incredible package and Python management tool jumped incredibly from 0% to 11% the year it was introduced (and that growth has demonstrably continued to surge in 2025).⁠⁠ This ⁠⁠ Rust-based tool unifies capabilities from many of the most important ones you may have previously heard of and does so with performance and incredible features.⁠⁠

Do you need Python on the machine? Simply `RUN uv venv .venv`, and you have both installed the latest stable release and created a virtual environment. ⁠⁠ That’s just the beginning. If you want the full story, I did [an interview with Charlie Marsh](https://talkpython.fm/episodes/show/453/uv-the-next-evolution-in-python-packages) about the second generation of uv over on *Talk Python*.⁠⁠

⁠⁠ If you decide to install uv, be sure to [use their standalone installers](https://github.com/astral-sh/uv?tab=readme-ov-file#installation). It allows uv to manage itself and get better over time.⁠⁠

⁠⁠ We saw that 83% of respondents are not using the latest version of Python. Don’t be one of them. Use a virtual environment or use a container and install the latest version of Python.⁠⁠ The ⁠⁠ quickest and easiest way these days is to use uv, as it won’t affect system Python and other configurations (see action 1!).⁠⁠

If you deploy or develop in Docker containers, all you need to do is set up the latest version of Python 3.13 and run these two lines:

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN uv venv --python 3.13 /venv

RUN curl -LsSf https://astral.sh/uv/install.sh | sh RUN uv venv --python 3.13 /venv

```
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN uv venv --python 3.13 /venv
```

If you develop locally in virtual environments (as I do), just remove the `RUN` keyword and use uv to create that environment. Of course, update the version number as new major versions of Python are released.

By taking this action, you will be able to ⁠⁠ take advantage of the full potential of modern Python, from the performance benefits to the language features.⁠⁠

If you’re one of the people who have not yet tried agentic AI, you owe it to yourself to give it a look. Agentic AI uses large language models (LLMs) such as GPT‑4, ChatGPT, or models available via Hugging Face to perform tasks autonomously.

I understand why people avoid using AI and LLMs. For one thing, there’s dubious legality around copyrights. The environmental harms can be real, and the threat to developers’ jobs and autonomy is not to be overlooked. But using top-tier models for *agentic* AI, not just chatbots, allows you to be tremendously productive.

⁠⁠ I’m not recommending vibe coding. But have you ever wished for a library or package to exist, or maybe a CLI tool to automate some simple part of your job? Give that task to an agentic AI, and you won’t be taking on technical debt to your main application and some part of your day. Your productivity just got way better.⁠⁠

The other mistake people make here is to give it a try using the cheapest or free models. When they don’t work that great, people hold that up as evidence and say, “See, it’s not that helpful. It just makes up stuff and gets things wrong.” Make sure you choose the best possible model that you can, and if you want to give it a genuine look, spend $10 or $20 for a month to see what’s actually possible.

JetBrains recently released [Junie, an agentic coding assistant for their IDEs](https://www.jetbrains.com/junie/). If you’re using one of them, definitely give it a look.

⁠⁠ Python developers should consider learning the basics of Rust, not to replace Python, but to complement it.⁠⁠ As I discussed in our analysis, Rust is becoming increasingly important in the most significant portions of the Python ecosystem. I definitely don’t recommend that you become a Rust developer instead of a Pythonista, but being able to read basic Rust so that you understand what the libraries you’re consuming are doing will be a good skill to have.

⁠⁠ Python developers have worked mainly outside the realm of threading and parallel programming. In Python 3.6, the amazing async and await keywords were added to the language. However, they only applied to I/O bound concurrency.⁠⁠ ⁠⁠ For example, if I’m calling a web service, I might use the HTTPX library and await that call. This type of concurrency mostly avoids race conditions and that sort of thing.⁠⁠

⁠⁠ Now, true parallel threading is coming for Python. With PEP 703 officially and fully accepted as part of Python in 3.14, we’ll need to understand how true threading works. This will involve understanding locks, semaphores, and mutexes.⁠⁠

⁠⁠ It’s going to be a challenge, but it is also a great opportunity to dramatically increase Python’s performance.⁠⁠

⁠⁠ At the 2025 Python Language Summit, almost one-third of the talks dealt with concurrency and threading in one form or another. This is certainly a forward-looking indicator of what’s to come.⁠⁠

⁠⁠ Not every program you write will involve concurrency or threading, but they will be omnipresent enough that having a working understanding will be important.⁠⁠ I have [a course I wrote about async in Python](https://training.talkpython.fm/courses/python-concurrency-deep-dive) if you’re interested in learning more about it. Plus, JetBrains’ own Cheuk Ting Ho wrote an excellent article entitled [*Faster Python: Concurrency in async/await and threading*](https://blog.jetbrains.com/pycharm/2025/06/concurrency-in-async-await-and-threading/), which is worth a read.

My final action to you is to keep things accessible for beginners – every time you build or share. Half of the Python developer base has been using Python for less than two years, and most of them have been programming in any format for less than two years. That is still remarkable to me.

So, as you go out into the world to speak, write, or create packages, libraries, and tools, remember that you should not assume years of communal knowledge about working with multiple Python files, virtual environments, pinning dependencies, and much more.

Interested in learning more? [Check out the full *Python Developers Survey* *Results* here](https://lp.jetbrains.com/python-developers-survey-2024/).

PyCharm provides everything you need for data science, ML/AI workflows, and web development right out of the box – all in one powerful IDE.

[Try PyCharm for free](https://www.jetbrains.com/pycharm/download/)

![Michael Kennedy](https://blog.jetbrains.com/wp-content/uploads/2024/11/michael-kennedy.jpg)

#### Michael Kennedy

Michael is the founder of Talk Python and a PSF Fellow. Talk Python is a podcast and course platform that has been exploring the Python ecosystem for over 10 years. At his core, Michael is a web and API developer.

- Share

[![](https://admin.blog.jetbrains.com/wp-content/uploads/2023/12/PyCharm_Python-IDE-for-data-and-web_970x250-2x.png)](https://www.jetbrains.com/pycharm/download/?utm_source=blog&utm_medium=banner&utm_campaign=mobile-apps#apps)

#### Subscribe to PyCharm Blog updates

![image description](https://blog.jetbrains.com/wp-content/themes/jetbrains/assets/img/img-form.svg)

[![10 Smart Performance Hacks For Faster Python Code](https://blog.jetbrains.com/wp-content/uploads/2025/10/PC-social-BlogFeatured-1280x720-1-20.png)](https://blog.jetbrains.com/pycharm/2025/11/10-smart-performance-hacks-for-faster-python-code/)

[Learn practical optimization hacks, from data structures to built-in modules, that boost speed, reduce overhead, and keep your Python code clean.](https://blog.jetbrains.com/pycharm/2025/11/10-smart-performance-hacks-for-faster-python-code/)

[![State of Django 2025](https://blog.jetbrains.com/wp-content/uploads/2025/10/Blog_1280x720-1.png)](https://blog.jetbrains.com/pycharm/2025/10/the-state-of-django-2025/)

[Develop with Django? See how over 4,600 developers are using it today and get actionable ideas to implement in your projects right now.](https://blog.jetbrains.com/pycharm/2025/10/the-state-of-django-2025/)

[![Why Performance Matters in Python Development](https://blog.jetbrains.com/wp-content/uploads/2025/10/PC-social-BlogFeatured-1280x720-1-8.png)](https://blog.jetbrains.com/pycharm/2025/10/why-performance-matters-in-python-development/)

[Learn why code optimization is important and how efficient Python code improves speed, scalability, and the user experience.](https://blog.jetbrains.com/pycharm/2025/10/why-performance-matters-in-python-development/)

[![Why Is Python So Popular in 2025?](https://blog.jetbrains.com/wp-content/uploads/2025/09/PC-social-BlogFeatured-1280x720-2x-8.png)](https://blog.jetbrains.com/pycharm/2025/09/why-is-python-so-popular/)

[From powering AI and data science to driving web development and automation, Python continues to dominate in 2025. Discover why in our blog post.](https://blog.jetbrains.com/pycharm/2025/09/why-is-python-so-popular/)

#to-finish

## Metadata

* URL: https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/
* description: Learn what 30,000 developers say about Python in 2025. Discover the latest survey stats, usage trends, and predictions to stay ahead in the Python world.
* date: 2025-08-18