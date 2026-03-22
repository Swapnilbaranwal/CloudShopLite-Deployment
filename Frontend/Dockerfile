FROM python:3.11-slim

WORKDIR /app

COPY app.py ./

# Pin pip version and install dependencies, then clean up
RUN pip install --upgrade pip==24.0 \
	&& pip install flask==3.0.3 requests==2.31.0 \
	&& rm -rf /root/.cache/pip

# Create non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 3000

CMD ["python", "app.py"]