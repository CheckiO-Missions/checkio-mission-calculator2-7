"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        # seventh
        {
            "input": ["100A90S"],
            "answer": "0",
        },
        {
            "input": ["100A90SG"],
            "answer": "10",
        },
        {
            "input": ["100A90EG"],
            "answer": "0",
        },
        {
            "input": ["ASG"],
            "answer": "0",
        },
        # sixth
        {
            "input": ["123BB"],
            "answer": "1",
        },
        {
            "input": ["123C12*=B"],
            "answer": "14",
        },
        {
            "input": ["123BBBBBB"],
            "answer": "0",
        },
        {
            "input": ["C"],
            "answer": "0",
        },
        {
            "input": ["-++B"],
            "answer": "0",
        },
        # fifth
        {
            "input": ["10/2*2="],
            "answer": "10.",
        },
        {
            "input": ["10/=*=-="],
            "answer": "0.",
        },
        {
            "input": ["100//33**3="],
            "answer": "27",
        },
        {
            "input": ["10%10="],
            "answer": "0",
        },
        {
            "input": ["---+++100//3//3+++---"],
            "answer": "11",
        },
        {
            "input": ["27**.3333="],
            "answer": "3.",
        },
        # fourth
        {
            "input": ["0001.1000"],
            "answer": "1.1",
            "explanation": "remove beg. adn trail. zeros",
        },
        {
            "input": ["999.9999999+="],
            "answer": "2000.",
            "explanation": "rounded to 5 digits",
        },
        {
            "input": ["1.000123"],
            "answer": "1.",
            "explanation": "remove trail. zeros after round",
        },
        {
            "input": ["9999.9999999+="],
            "answer": "error",
            "explanation": "int. part is bigger then 9999",
        },
        # third
        {
            "input": ["90000+10000="],
            "answer": "error",
            "explanation": "too many digits in the result",
        },
        {
            "input": ["90000+10000-10000="],
            "answer": "error",
            "explanation": "any operation after error doesn't fix the error",
        },
        {
            "input": ["90000+10000-10000"],
            "answer": "10000",
            "explanation": "last entered number is shown even with error",
        },
        {
            "input": ["123456789"],
            "answer": "12345",
            "explanation": "only first 5 digits are shown",
        },
        {
            "input": ["123456789+5="],
            "answer": "12350",
            "explanation": "Only first 5 digits are used in the operation",
        },
        {
            "input": ["5+123456789"],
            "answer": "12345",
            "explanation": "5 digits of last number entered",
        },
        {
            "input": ["50000+="],
            "answer": "error",
            "explanation": "result has length of 6 digits",
        },
        # second
        {
            "input": ["3+="],
            "answer": "6",
            "explanation": "3+= is the same as 3+3=",
        },
        {
            "input": ["3+2=="],
            "answer": "7",
            "explanation": "the same as 3+2+2=",
        },
        {
            "input": ["3+-2="],
            "answer": "1",
            "explanation": "the last sign is taken",
        },
        {
            "input": ["-=-+3-++--+-2=-"],
            "answer": "1",
            "explanation": "the last sign is taken, ignore beginning signs",
        },
        # first
        {
            "input": ["000000"],
            "answer": "0",
            "explanation": "single zero instead of multi-zeros number",
        },
        {
            "input": ["0000123"],
            "answer": "123",
            "explanation": "remove beginning zeros",
        },
        {
            "input": ["12"],
            "answer": "12",
            "explanation": "you see what you enter",
        },
        {
            "input": ["+12"],
            "answer": "12",
            "explanation": "ignore beginning operations",
        },
        {
            "input": [""],
            "answer": "0",
            "explanation": "when power on - 0 on the screen",
        },
        {
            "input": ["1+2"],
            "answer": "2",
            "explanation": "last entered number, no operations after",
        },
        {
            "input": ["2+"],
            "answer": "2",
            "explanation": "single +/- do nothing",
        },
        {
            "input": ["1+2="],
            "answer": "3",
            "explanation": "standard operation",
        },
        {
            "input": ["1+2-"],
            "answer": "3",
            "explanation": "last sign requires previous calculations to be done",
        },
        {
            "input": ["1+2=2"],
            "answer": "2",
            "explanation": "entering number rewrites previous result",
        },
        {
            "input": ["=5=10=15"],
            "answer": "15",
        },
    ],
    "Extra": [
        # seventh
        {
            "input": ["36/5AG"],
            "answer": "5",
        },
        {
            "input": ["36/5*A5*G=B"],
            "answer": "36",
        },
        {
            "input": ["10*=A80S2*G+="],
            "answer": "80",
        },
        {
            "input": ["12**2AG"],
            "answer": "2",
        },
        {
            "input": ["12**2-AG"],
            "answer": "144",
        },
        # sixth
        {
            "input": ["999*=C99*=B"],
            "answer": "980",
        },
        {
            "input": ["2+3.==B"],
            "answer": "8",
        },
        {
            "input": ["88.*=B*10"],
            "answer": "10",
        },
        {
            "input": ["12=B"],
            "answer": "1",
        },
        {
            "input": ["12+B"],
            "answer": "12",
        },
        {
            "input": ["12+B-B*B/B//BB2"],
            "answer": "122",
        },
        # fifth
        {
            "input": ["25**000.5000="],
            "answer": "5.",
        },
        {
            "input": ["999*="],
            "answer": "error",
        },
        {
            "input": ["99.99*="],
            "answer": "9998.",
        },
        {
            "input": ["110/10"],
            "answer": "10",
        },
        {
            "input": ["110/10="],
            "answer": "11.",
        },
        {
            "input": ["110//10="],
            "answer": "11",
        },
        {
            "input": ["110%10="],
            "answer": "0",
        },
        # fourth
        {
            "input": ["0001.2005+=-1+10.43+99979"],
            "answer": "99979",
        },
        {
            "input": ["0001.2005+=-1+10.43+99979="],
            "answer": "error",
        },
        {
            "input": ["-+++--+.12009"],
            "answer": ".12",
        },
        {
            "input": ["999.999+========="],
            "answer": "9999.",
        },
        # third
        {
            "input": ["100000"],
            "answer": "10000",
        },
        {
            "input": ["99999+1"],
            "answer": "1",
        },
        {
            "input": ["99999+1="],
            "answer": "error",
        },
        {
            "input": ["50000+49999="],
            "answer": "99999",
        },
        {
            "input": ["50000+50000+2="],
            "answer": "error",
        },
        {
            "input": ["50000+50000+2"],
            "answer": "2",
        },
        {
            "input": ["50000-===="],
            "answer": "error",
        },
        # second
        {
            "input": ["78-="],
            "answer": "0",
        },
        {
            "input": ["3+2-="],
            "answer": "0",
        },
        {
            "input": ["+-=12="],
            "answer": "12",
        },
        {
            "input": ["2+3=+7="],
            "answer": "12",
        },
        {
            "input": ["2+3=7+7="],
            "answer": "14",
        },
        {
            "input": ["12+15=="],
            "answer": "42",
        },
        # first
        {
            "input": ["000005+003"],
            "answer": "3",
        },
        {
            "input": ["000005+003="],
            "answer": "8",
        },
        {
            "input": ["-5-10+15"],
            "answer": "15",
        },
        {
            "input": ["-5-10+15-"],
            "answer": "10",
        },
        {
            "input": ["+1+2+3+4="],
            "answer": "10",
        },
        {
            "input": ["+"],
            "answer": "0",
        },
    ]
}
