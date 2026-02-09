# GSTT MRI Computing

Welcome to the MRI Computing GitHub! 

![](readme-resources/screenshot.jpg)


Please ensure you have downloaded GitHub Desktop on your computer. You can optionally use Git from the command line, however this is not recommended if you have not frequently worked with GitHub. Firstly, open a terminal, and run the command:

```bash
cd Documents
```

Then run:

```bash
ls 
```

To see if there is a folder called GitHub. If there is a folder already, skip to the next step, if there is not, run:

```bash
mkdir GitHub
cd GitHub 
```

Then, run:

```python
git clone https://github.com/GSTT-MRI-Computing/main_database.git
```

Any new projects must be made inside the projects tab. All code needs to be modular, i.e. write as much of it as self-contained functions as possible. When you have written a function, save it as a file in the appropriate folder, under the functions directory.
To start your new project, first create a new folder in the projects tab, and then create a requirements.txt file, containing all of the modules you intend to use. When you have navigated to your new project folder and want to download the correct packages, run:

```python
python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt
```

Ensure that the main script is called main.py, and that it takes its functions from the functions folder, as this is where you will be saving all functions. 
Ensure when you have written your function, you comment on what is used as an input and what is the expected output, so that the GitHub administrator can set up a test for your function.
If you are someone with experience in GitHub. modify the test scripts in the tests tab to seamlessly integrate your function into GitHub actions.
Importing your newly saved function in your script will usually look like:

```python
from ../functions.filepaths.my_function import my_function
```

```python
python3 main.py
```
