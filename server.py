from flask import Flask, jsonify, make_response
import asyncio
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)

@app.route('/common/updateBinary', methods=['POST'])
async def test():
    asyncio.create_task(process_request())
    return make_response("", 201)

async def process_request():
    print("Start Processing")
    for _ in range(100000):
        print('call')
        await asyncio.sleep(0)  # 가정: 비동기 작업이 1초 동안 실행됩니다.
    print("End Processing request...")

# Flask 애플리케이션을 ASGI 애플리케이션으로 변환
asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=5050)
