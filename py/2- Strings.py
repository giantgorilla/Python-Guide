{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e9d98b65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "10841e62",
   "metadata": {},
   "outputs": [],
   "source": [
    "name = \"Doğukan\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d2dcf4c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f8bfbc15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HelloDoğukan\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello\" +name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1991a93f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#İlk örnekte görüldüğü gibi arada boşluk yok. Boşluk koymak için;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4e9cd30c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Doğukan\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello\", \"\" +name) #Ekstra bir string oluşturulur lâkin boş bırakılır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "117d7ec2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nname. yazıp tab tuşuna basarak gerçekleştirilebilecek işlemleri görebilirsiniz.\\nDaha önce yukarıda tanımlanmış olan bir değeri print fonksiyonuna +degisken\\nyazarak printout alabilirsiniz.\\n'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "name. yazıp tab tuşuna basarak gerçekleştirilebilecek işlemleri görebilirsiniz.\n",
    "Daha önce yukarıda tanımlanmış olan bir değeri print fonksiyonuna +degisken\n",
    "yazarak printout alabilirsiniz.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "00034006",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Doğukan'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.capitalize() #Değişkenin ilk harfini büyük yapar. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "34533c84",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function count:\n",
      "\n",
      "count(...) method of builtins.str instance\n",
      "    S.count(sub[, start[, end]]) -> int\n",
      "    \n",
      "    Return the number of non-overlapping occurrences of substring sub in\n",
      "    string S[start:end].  Optional arguments start and end are\n",
      "    interpreted as in slice notation.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(name.count) #Count hakkında bilgi verir. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fcc9e76d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.count(\"a\") #Name değişkeni içerisinde kaç adet a harfi olduğunu sayar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f934982f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.count(\"b\") #Name değişkeni içerisinde kaç adet b harfi olduğunu sayar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9fd7821a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'DOĞUKAN'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.upper() #Name değişkeninin tüm harflerini büyük harf yapar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5baa6480",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(name) #lenght = değişkenin uzunluğunu, karakter sayısını verir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "69e14207",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello \n",
      "Doğukan\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello \\n\" +name) # \\n -> New Line = Alt satıra geç anlamına gelir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "ce447d0b",
   "metadata": {},
   "outputs": [],
   "source": [
    "name = \"Doğukan\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "3e3520c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "surname = \"Bostancı\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "45818f41",
   "metadata": {},
   "outputs": [],
   "source": [
    "fullName = name + \" \" + surname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "29210fcd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Doğukan Bostancı'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fullName"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2249e809",
   "metadata": {},
   "source": [
    "# Index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bfe13fc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "myString = \"Doğukan Bostancı\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "12e3217a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'k'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myString[4] #Index değeri '0'dan başlar ve her karakter (boşluk dahil) sayılır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2d8dbb2c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(myString)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f0c842d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(myString) - 1 #Son değeri verir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b3f44132",
   "metadata": {},
   "outputs": [],
   "source": [
    "myName = \"James Hetfield\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3fd96f9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(myName) - 1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "af9f0366",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myName[13]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "8697d710",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myName[-1] #Indexi tersten döndürmeye başlar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "56d15d73",
   "metadata": {},
   "outputs": [],
   "source": [
    "barcode = \"ABCDE123123982\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "5d462bd6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ABC'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "barcode[0] + barcode[1] + barcode[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16ae2959",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Slicing, starting index, stopping index, stepping size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "d0dc1e85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ABC'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "barcode[0:3:1] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "e5fc93e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'DE123123982'"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "barcode[3::]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "9c84e8d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'289321321EDCBA'"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "barcode[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "460d2d4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myString.index(\"k\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "de7ad934",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Doğukan', 'Bostancı']"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myString.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36deb131",
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
