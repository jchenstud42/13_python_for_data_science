import time
import datetime

BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"


# returns time in seconds since January 1, 1970
seconds_since_epoch = time.time()
formatted_seconds = f"{seconds_since_epoch:,}"
scientific_format = "{:e}".format(seconds_since_epoch)

date_rn = datetime.datetime.now()
formatted_date = date_rn.strftime("%b %d %Y")


print(
    "\n",
    BOLD + "Seconds since January 1, 1970 :" + RESET,
    BLUE + formatted_seconds + RESET,
    "or",
    BLUE + scientific_format + RESET,
    "in scientific notation\n",
    BOLD + formatted_date + RESET,
    "\n",
)
