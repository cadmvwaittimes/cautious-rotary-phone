import os
from dotenv import load_dotenv


load_dotenv()

config = dict(
    python_exc=os.environ['CADMV_PYTHON_EXC'],
    test_script=os.environ['CADMV_PYTHON_TEST_SCRIPT']
)
