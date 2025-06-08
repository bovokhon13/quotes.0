from aiogram.fsm.state import State, StatesGroup

class QuoteStates(StatesGroup):
    waiting_for_quote_index = State()
