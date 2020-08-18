# API Routes

## /lighting/ringlight

### GET /
returns a list of lights available

### POST /set_color
required body: 
```json
{
        "light_id": "string",
        "r": "0 < int < 255",
        "g": "0 < int < 255",
        "b": "0 < int < 255",
        "brightness": "0 < int < 255"
}
```
response:  
OK or ERROR message

### POST /set_frame
required body:
```json
{
    "light_id": "string",
    "frame": "an array of length 36 made of [int, int, int]",
    "brightness": "int"
}
```