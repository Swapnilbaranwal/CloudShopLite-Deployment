FROM python:3.11-slim

WORKDIR /app

COPY . ./

# Pin pip version, install dependencies, clean up
RUN pip install --upgrade pip==24.0 \
	&& pip install -r requirements.txt \
	&& rm -rf /root/.cache/pip

# Create non-root user
RUN useradd -m appuser
USER appuser

CMD ["python", "worker.py"]