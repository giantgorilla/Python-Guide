{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "36fdbd62",
   "metadata": {},
   "source": [
    "# Method vs Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6ff3f7af",
   "metadata": {},
   "outputs": [],
   "source": [
    "myName = \"Doğukan\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "df47d928",
   "metadata": {},
   "outputs": [],
   "source": [
    "def hello():\n",
    "    print(\"Hello\")\n",
    "    print(\"Python\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "888fe20a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "Python\n"
     ]
    }
   ],
   "source": [
    "hello()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d560e0ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "def hello_name(name):\n",
    "    print(\"hello\")\n",
    "    print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "52d43068",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "Doğukan\n"
     ]
    }
   ],
   "source": [
    "hello_name(\"Doğukan\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e77f71f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def sumExample(num1, num2):\n",
    "    print(num1 + num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ac531aa2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "26\n"
     ]
    }
   ],
   "source": [
    "sumExample(12, 14)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa9c2864",
   "metadata": {},
   "outputs": [],
   "source": [
    "def summation(n1, n2, n3):\n",
    "    print(n1+n2+n3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b4a2fa28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "44\n"
     ]
    }
   ],
   "source": [
    "summation(10, 23, 11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "28461c53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "44\n"
     ]
    }
   ],
   "source": [
    "x = summation(10, 23, 11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4fc64843",
   "metadata": {},
   "outputs": [],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a7565e98",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0727ee71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "NoneType"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7b4f4c06",
   "metadata": {},
   "outputs": [],
   "source": [
    "def returnSummation(n1, n2, n3):\n",
    "    return n1+n2+n3 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "46370ada",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = returnSummation(10, 23, 11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "80c9a8c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "44"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a6a7a8cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def controlString(s):\n",
    "    if s[0] == \"a\":\n",
    "        print(\"A\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2a3935fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    }
   ],
   "source": [
    "controlString(\"atlas\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f68f6b68",
   "metadata": {},
   "outputs": [],
   "source": [
    "controlString(\"James\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a8706438",
   "metadata": {},
   "source": [
    "# Args, Kwargs (Arguments, Key Word Arguments)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9f86138f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def argsSum(*args):\n",
    "    return sum(args)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e9c0e3e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "210"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "argsSum(10, 20, 30, 40, 50, 60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "55ea7c61",
   "metadata": {},
   "outputs": [],
   "source": [
    "def argsExample(*args):\n",
    "    print(args)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "60bb893e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(123, 12312310, 343, 123, 34)\n"
     ]
    }
   ],
   "source": [
    "argsExample(123, 12312310, 343, 123, 34)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1dfaa745",
   "metadata": {},
   "outputs": [],
   "source": [
    "def kwargsExample(**kwargs):\n",
    "    print(kwargs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "38014ac1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'apple': 100, 'banana': 150, 'melon': 200}\n"
     ]
    }
   ],
   "source": [
    "kwargsExample(apple = 100, banana = 150, melon = 200)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "30e9af1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def kwargsExample2(**kwargs):\n",
    "    if \"apple\" in kwargs:\n",
    "        print(\"Apple\")\n",
    "    else:\n",
    "        print(\"Wrong!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a89b1df5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Apple\n"
     ]
    }
   ],
   "source": [
    "kwargsExample2(apple = 10, banana = 15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1f6cc69e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong!\n"
     ]
    }
   ],
   "source": [
    "kwargsExample2(banana = 15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19069c2b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
