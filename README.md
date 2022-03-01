# ML TEST UMBA

## Instructions
## Stage 1
Install requirements.txt
```console
pip install requirements.txt
```
run
```console
python app/seed.py
```
Command without -t <total records> or -total <total records>  flag will pull all records 
```console
python app/seed.py -t <amount>
python app/seed.py --total <amount>
```

## Stage 2
Run
```console
python app/app.py
```

View grid with default 25 records page 1
```http
localhost:5000/users
```
Modify pagination
```http
localhost:5000/users?pagination=<amount>
```

