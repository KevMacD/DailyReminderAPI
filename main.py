import json
from typing import Optional
from fastapi import FastAPI
# git add .
# git commit -m "message"
# git push origin main
# https://dailyreminderapi.onrender.com
# https://dailyreminderapi.onrender.com/items/12
# https://dashboard.render.com/web/srv-d5hc3jadbo4c73dtsh3g/deploys/dep-d5hcstq4d50c7390mlk0


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/settings/")
def get_settings():
    return read_file("settings.txt")

@app.put("/settings/")
def update_settings(data: dict):
    if data["kyber"]=="crystal":
        data["Yes"]="Password"        
        del data["kyber"]

    json_string = json.dumps(data)
    respone_dict = save_file("settings.txt",json_string)
    return save_file("settings.txt",json_string)


def save_file(file_path:str,file_content:str)->{}: # type: ignore
    try:
        with open(file_path, "w") as file:
            file.write(file_content)
            return_dict["response"]= True # type: ignore
    except Exception as e:
        return 
        return_dict["response"]= False # type: ignore
        return_dict["message"] =f"An error occurred while saving the file: {e}" # type: ignore

def read_file(file_path:str)->{}: # type: ignore
    return_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return_dict["response"]=True # type: ignore
            return_dict["message"]= "API:File Found and succesfully Read" # type: ignore
            return_dict["data"]=content # type: ignore
            return return_dict
    except FileNotFoundError:
        return_dict["response"]= False # type: ignore
        return_dict["message"] =f"API Error: The file '{file_path}' was not found." # type: ignore
        return_dict["data"]=Null # type: ignore
        return return_dict
    except Exception as e:
        return_dict["response"]= False # type: ignore
        return_dict["message"] =f"API: An error occurred while reading the file: {e}" # type: ignore
        return_dict["data"]=Null # type: ignore
        return return_dict