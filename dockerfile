FROM ghcr.io/railwayapp/nixpacks:ubuntu-1716249803

WORKDIR /app/

# Copy Nixpacks configuration
COPY .nixpacks/nixpkgs-bf446f08bff6814b569265bef8374cfdd3d8f0e0.nix .nixpacks/nixpkgs-bf446f08bff6814b569265bef8374cfdd3d8f0e0.nix

# Install nix packages
RUN nix-env -if .nixpacks/nixpkgs-bf446f08bff6814b569265bef8374cfdd3d8f0e0.nix && nix-collect-garbage -d

# Copy project files
COPY . /app/

# Create and activate virtual environment, then install dependencies
RUN python -m venv --copies /opt/venv && . /opt/venv/bin/activate && pip install -r requirements.txt

# Set the entrypoint
CMD ["gunicorn", "faceidnazorat.wsgi"]
