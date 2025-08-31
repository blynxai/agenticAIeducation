## Master AI Agentic Engineering -  build autonomous AI Agents

# Setting up WSL - Windows Subsytem for Linux

_NOTE 1: These instructions assume that you've already carried out the PC Setup instructions_

_NOTE 2: In Cursor, remember to Right Click on this file in the Explorer and choose "Open Preview" to see the formatting._

Welcome back to Setup-land, PC people!

I expect you're here because you've reached Week 6, and discovered the unpleasant news that MCP Servers are only working on Windows under WSL.

I'm so sorry to put you through this! The good news is, several students have confirmed that MCP Servers are working under WSL. Also, WSL is generally considered a great way to build on Windows. And the other good news is that you've already done the setup once, so surely this will be relatively painless? Fingers crossed.

### Part 1: Install WSL if you haven't before

WSL is the Microsoft recommended way to run Linux on your Windows PC, as described here:  
https://learn.microsoft.com/en-us/windows/wsl/install

We will be using the default Ubuntu distribution of Linux, which seems to work fine. Let's do this!

1. Open a powershell
2. Run: `wsl --install`
3. Select to allow elevated permissions when it asks; then wait for Ubuntu to install
4. Then run `wsl` to start it and set your Linux username and password
5. Type `pwd` and `ls` to see what directory you're in, and list the contents. Then type `cd` to change to your home directory, and repeat.

It's important to appreciate the difference between your Windows home directory, and this new home directory in your Linux WSL world..

### Part 2: Install uv and repo

1. In a WSL window (i.e. a Powershell after you've typed 'wsl') - we will follow the linux instructions here: https://docs.astral.sh/uv/getting-started/installation/ and run `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. After that completes, you need to type `exit` to leave WSL and restart your PC
3. Return to the Powershell and then type `wsl` to return to Linux, in order that changes to PATH are picked up
4. Now type `cd` to go to your Linux home directory. Check you're there with `pwd` and `ls`
5. Now create a projects directory with `mkdir projects` then `cd projects` to go into it
6. And, from within your new projects directory, clone the repo with `git clone https://github.com/blynxai/agenticaieducation.git`
7. Now go into your new agents directory, your Project Root Directory, with `cd agenticAIeducation`
8. And now run the all-powerful `uv sync`

### Part 3: Install Node if you haven't done so yet (this is required for Playwright)
1. In your WSL environment open a terminal and install nvm: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`
2. Close and repoen Cursir and restart your WSL enviornment in the rocess
3. Activate your virtual environment with `.venv\Scripts\Avtivate.ps1`
4. Intall your latest version of Node with `nvm install --lts`
5. Confirm the installation by typing `node -v`

### Part 4: Configure Cursor running in your PC environment

1. Open Cursor, the usual way, on your PC
2. Bring up the Extensions panel (View menu >> Extensions or Ctrl+Shift+X), search for WSL, see WSL by Anysphere (the makers of Cursor) and Install it
3. Now press Ctrl+Shift+P and search for Remote-WSL: New Window and select it to Open a new window configured for WSL
4. Select Open Project (then get a coffee), and navigate to your new "agents" project root directory in Linux, and then Open or Select Folder
5. Bring up the Extensions panel again (Ctrl+Shift+X) and install these Extensions in your WSL if not already installed: Python (ms-python), and Jupyter (microsoft), clicking the "Install in WSL-Ubuntu" button
6. Restart your cursor and follow the steps above to return to your WSL environment

### And you should be ready to roll!

You'll need to create a new ".env" file in the agents folder, and copy across your .env from your other project. And you'll need to click "Select Kernel" and "Choose python environment..".

Enjoy MCP!