from fastapi import APIRouter, HTTPException
from app.services.nlp_parser import parse_trade_instruction, TradeParseError
from app.db.trade_queue import add_trade
from app.db.trade_queue import get_all_trades

router = APIRouter(prefix="/api")

@router.post("/chat")
def chat_endpoint(request: dict):
    message = request.get("text")
    try:
        parsed_trade = parse_trade_instruction(message)
        add_trade(parsed_trade)
        return {"parsed_trade": parsed_trade}
    
    except TradeParseError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/chat/trades")
def get_saved_trades():
    return {"trades": get_all_trades()}