from flask_restful import Resource
from aiohttp.client import ClientSession 
import asyncio
import json

USERS_LIST = [
    'AlexandreSouzaRocha',
    'diego3g'
]
class AsynchronousResource (Resource):

    async def get_github_profile(self, user_name, session):
        url = 'https://api.github.com/users/{0}'.format(user_name)
        async with session.get(url) as response:
            return await response.read()
    
    async def get_futures(self, users_list):
        users = []
        data = []    
        async with ClientSession() as session:
            for user in users_list:
                future = asyncio.ensure_future(self.get_github_profile(user, session))
                users.append(future)    
            response = await asyncio.gather(*users)
        
            for item in response:
                data.append(json.loads(item.decode('utf-8')))
        
        return data

    def do_requests(self, loop):
        asyncio.set_event_loop(loop)
        futures = asyncio.ensure_future(self.get_futures(USERS_LIST))
        response = loop.run_until_complete(futures)

        return response
    
    def get(self):
        loop = asyncio.new_event_loop()
        users = self.do_requests(loop)

        return {
            'users': users
        }, 200