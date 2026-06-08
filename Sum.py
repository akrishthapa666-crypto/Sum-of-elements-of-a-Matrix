{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red202\green202\blue202;
\red67\green192\blue160;\red212\green212\blue212;\red212\green214\blue154;\red194\green126\blue101;\red188\green135\blue186;
\red113\green184\blue255;\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\csgray\c100000;\cssrgb\c83137\c83137\c83137;
\cssrgb\c30588\c78824\c69020;\cssrgb\c86275\c86275\c86275;\cssrgb\c86275\c86275\c66667;\cssrgb\c80784\c56863\c47059;\cssrgb\c78824\c61176\c77647;
\cssrgb\c50980\c77647\c100000;\cssrgb\c70980\c80784\c65882;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 rows=\strokec5 int\strokec6 (\strokec7 input\strokec6 (\strokec8 "Enter the number of rows: "\strokec6 ))\strokec4 \
cols=\strokec5 int\strokec6 (\strokec7 input\strokec6 (\strokec8 "Enter the number of columns:"\strokec6 ))\strokec4 \
\
matrix=\strokec6 []\strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec9 for\strokec4  i \strokec10 in\strokec4  \strokec7 range\strokec6 (\strokec4 rows\strokec6 ):\strokec4 \
  row=\strokec5 list\strokec6 (\strokec7 map\strokec6 (\strokec5 int\strokec6 ,\strokec7 input\strokec6 ()\strokec4 .split\strokec6 ()))\strokec4 \
  matrix.append\strokec6 (\strokec4 row\strokec6 )\strokec4 \
\
sum=\strokec11 0\strokec4 \
\strokec9 for\strokec4  i \strokec10 in\strokec4  \strokec7 range\strokec6 (\strokec4 rows\strokec6 ):\strokec4 \
  \strokec9 for\strokec4  j \strokec10 in\strokec4  \strokec7 range\strokec6 (\strokec4 cols\strokec6 ):\strokec4 \
    sum+=matrix\strokec6 [\strokec4 i\strokec6 ][\strokec4 j\strokec6 ]\strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec7 print\strokec6 (\strokec8 "sum="\strokec6 ,\strokec4 sum\strokec6 )\strokec4 \
}