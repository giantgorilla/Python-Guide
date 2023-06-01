{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7461b8b1",
   "metadata": {},
   "source": [
    "# Try - Except"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6a112148",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your Age: 35\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    \n",
    "    try:\n",
    "        myAge = int(input(\"Enter Your Age: \"))\n",
    "        break\n",
    "    except ValueError: \n",
    "        print(\"Enter Your Age!:\")\n",
    "    else: \n",
    "        print(\"Else Executed\")\n",
    "    finally:\n",
    "        print(\"Finally\")"
   ]
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
