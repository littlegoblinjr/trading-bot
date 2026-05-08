import bot.logging_config
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os

# Import your existing bot logic
from bot.orders import create_order
from bot.validators import validate_order

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Mount static files for the frontend (production build)
DIST_DIR = os.path.join("frontend", "dist")
if not os.path.exists(DIST_DIR):
    os.makedirs(DIST_DIR, exist_ok=True)

if os.path.exists(os.path.join(DIST_DIR, "assets")):
    app.mount("/assets", StaticFiles(directory=os.path.join(DIST_DIR, "assets")), name="assets")

@app.get("/")
async def read_index():
    index_path = os.path.join(DIST_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Frontend build not found. Run the build script."}

class OrderRequest(BaseModel):
    symbol: str
    side: str
    typee: str
    quantity: float
    price: Optional[float] = None
    stop_price: Optional[float] = None

@app.post("/api/order")
async def place_order(order: OrderRequest):
    try:
        order_data = order.dict()
        validate_order(order_data)
        
        response = create_order(
            symbol=order.symbol,
            side=order.side,
            typee=order.typee,
            quantity=order.quantity,
            price=order.price,
            stop_price=order.stop_price
        )
        
        if response:
            return {"status": "success", "data": response}
        else:
            raise HTTPException(status_code=400, detail="Order failed at exchange")
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/logs")
async def get_logs():
    log_path = os.path.join("bot", "logs", "trading.log")
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            # Send last 20 logs
            return {"logs": f.readlines()[-20:]}
    return {"logs": []}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
