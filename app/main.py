import uvicorn

if __name__ == '__main__':
    uvi_config = uvicorn.Config("server:app", port=5000, log_level="info")
    server = uvicorn.Server(uvi_config)
    server.run()