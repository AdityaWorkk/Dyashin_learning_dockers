FROM Python:3.11-slim

WORKDIR /Dyashin_Cloud


#Copy requires atleast two arguments
COPY requirements.txt .

#"--no-cache-dir" important because when we change 
#anything in the main directory the docker does have to reinstall it

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn","fastapi_app:app","--host","0.0.0.0","--post","8000"]
