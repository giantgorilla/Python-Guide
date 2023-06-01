{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1) Aşağıdaki kodun çıktısı ne olacaktır?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "def toplama(a,b):\n",
    "    print(a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 4\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "x = toplama(3,4)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2) Aşağıdaki kodun çıktısı ne olacaktır?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def usselIslem(x=5,y=3):\n",
    "    print(x ** y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n"
     ]
    }
   ],
   "source": [
    "usselIslem(2,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#3) Aynı fonksiyonu aşağıdaki gibi çağırırsak çıktı ne olur?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "125\n"
     ]
    }
   ],
   "source": [
    "usselIslem()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#4) Aşağıdaki kodun çıktısı ne olacaktır?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myLoop(*args):\n",
    "    for element in args:\n",
    "        print(element / 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.5\n",
      "1.0\n",
      "0.5\n",
      "2.5\n",
      "1.5\n",
      "2.0\n"
     ]
    }
   ],
   "source": [
    "myLoop(3,2,1,5,3,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#5) Aşağıdaki dizide belirtilen rakamları, myFunction fonksiyonuna tabi tutup, yeni bir dizi oluşturunuz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myFunc(num):\n",
    "    return num ** 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [2,3,4,5,6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[8, 27, 64, 125, 216]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(myFunc, myList))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "#6) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "barkodDizisi = [\"ABC231\",\"SA3123XYZ\",\"XYZA123Q\",\"QRE1231KJ\",\"X112QGL\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['SA3123XYZ', 'XYZA123Q']"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(filter(lambda string : \"XYZ\" in string, barkodDizisi))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#7) Aşağıdaki kodu okursanız, ornekFonksiyon çalıştırıldığında en altta yazdırılan print size neyi yazdıracaktır?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "myVar = \"Atil Samancioglu\"\n",
    "\n",
    "def ornekFonksiyon():\n",
    "    myVar = \"Atil\"\n",
    "    \n",
    "    def digerFonksiyon():\n",
    "        print(myVar)\n",
    "    \n",
    "    digerFonksiyon()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Atil\n"
     ]
    }
   ],
   "source": [
    "ornekFonksiyon()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "#8) Aşağıda yazdırılan sınıfı incelediğinizde kedim.yasiCarp() kodunun çıktısı ne olacaktır?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Kedi():\n",
    "        \n",
    "    def __init__(self,isim,yas=5):\n",
    "        self.isim = isim\n",
    "        self.yas = yas\n",
    "        \n",
    "    def yasiCarp(self):\n",
    "        return self.yas * 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "kedim = Kedi(\"Tonton\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kedim.yasiCarp()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "#9) Aşağıdaki kodun çıktısı ne olacaktır?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Ogrenci():\n",
    "    \n",
    "    def __init__(self,isim,sinavNotu):\n",
    "        self.isim = isim\n",
    "        self.__sinavNotu = sinavNotu\n",
    "    \n",
    "    def notuGoster(self):\n",
    "        print(f\"{self.isim} sınav notu: {self.__sinavNotu}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "ogrenci = Ogrenci(\"Mehmet\",85)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "ogrenci.__sinavNotu = 75"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mehmet sınav notu: 85\n"
     ]
    }
   ],
   "source": [
    "ogrenci.notuGoster()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "#10) Soyut sınıflar ve methodlar oluşturmamıza olanak tanıyan, kodlarımızı daha planlı şekilde yazmamızı mümkün kılan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "# aynı zamanda büyük projelerde bize yapısal olarak fayda sağlayabilecek OOP prensibinin adı nedir?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Abstraction"
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
 "nbformat_minor": 4
}
