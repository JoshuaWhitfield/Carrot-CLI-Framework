# carrot-cli-framwork
This is a data collection cli for AI model training and development

<h1>Getting Started:</h1>
<p>clone the repository and download the following dependencies:</p>

```bash
    # $ clone the repository

    $ python -m venv carrot-cli-fw

    $ carrot-cli-fw\Scripts\activate

    # import your required modules for your project
    # examples listed below

    $ python -m pip install requests

    $ python -m pip install beautifulsoup4

    $ python -m pip install validators

```

<h1>Tokenization:</h1>
<p>tokens that hold no value or a predefined value are instantiated like this:</p>

```python
    # All Tokens Available
    from syntax.tokens.TokenTypes import TokenTypes
    TT = TokenTypes()

    # words and strings
    command_token = TT.Command() # { "type": "COMMAND", "value": None }
    string_token = TT.String() # { "type": "STRING", "value": None }
    flag_token = TT.Flag() # { "type": "FLAG", "value": None }
    global_flag_token = TT.GlobalFlag() # { "type": "GLOBALFLAG", "value": None }
    macro_token = TT.Macro() # { "type": "COMMAND", "value": None }

    # numbers and symbols
    number_token = TT.Number() # { "type": "NUMER", "value": None }
    lparen_token = TT.LParen() # { "type": "LPAREN", "value": None }
    rparen_token = TT.RParen() # { "type": "RPAREN", "value": None }
    Assign = TT.Assign() # { "type": "ASSIGN", "value": None }

```

<p>you access these tokens through their methods, see ./syntax/tokens/LexerTokens</p>

<p>feel free to add your own tokens, but remember to capture them in the lexer and parser to capture them and tokenize them with regex. Also make changes to the interpreter depending on the case.</p>

<h1>Interpretation:</h1>
<h1>Creating Commands:</h1>
<h1>Accessing Piping:</h1>
