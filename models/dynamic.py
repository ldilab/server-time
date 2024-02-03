from app import db


class DynamicCPUModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    used_percent = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<DynamicCPUModel @{self.servername} ({self.cpu_used_percent}%)>'


class DynamicMemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    available_percent = db.Column(db.Float, nullable=False)
    available_gb = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<DynamicMemoryModel @{self.servername} ({self.available_percent}% - {self.available_gb}GB)>'


class DynamicDiskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    diskname = db.Column(db.String(80), nullable=False)
    free_percent = db.Column(db.Float, nullable=False)
    free_gb = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<DynamicDiskModel @{self.servername} ({self.diskname} - {self.free_percent}% - {self.free_gb}GB)>'


class DynamicGPUModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    device_id = db.Column(db.Integer, nullable=False)
    free_percent = db.Column(db.Float, nullable=False)
    free_gb = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<DynamicGPUModel @{self.servername} ({self.device_id} - {self.free_percent}% - {self.free_gb}GB - {self.temperature}C)>'


class DynamicImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    short_id = db.Column(db.String(80), unique=True, nullable=False)
    tag = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<DynamicImageModel @{self.servername} ({self.short_id} - {self.tag})>'


class DynamicContainerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    container_id = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)
    image_tag = db.Column(db.String(80), unique=False, nullable=False)
    mountpoint = db.Column(db.String(80), unique=False, nullable=False)
    started_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<DynamicContainerModel @{self.servername} ({self.container_id} - {self.name} - {self.status} - {self.image_tag})>'

