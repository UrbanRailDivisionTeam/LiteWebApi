import datetime
from fastapi import APIRouter

from utils import connect

router = APIRouter(prefix='/api')


@router.get('/update_time/{coll_name}')
async def get_udpate_time(coll_name: str):
    coll = connect['liteweb']['update_time']
    update_time = coll.find_one({'name': coll_name})
    if update_time is None:
        return {'time': datetime.datetime.min}
    else:
        return {'time': str(update_time['time'])}
