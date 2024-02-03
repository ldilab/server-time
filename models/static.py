from app import db


class StaticCPUModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    count = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'<StaticCPU @{self.servername} (cnt:{self.count})>'


class StaticMemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    total_gb = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<StaticRAM @{self.servername} (total_gb:{self.total_gb})>'


class StaticDiskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    diskname = db.Column(db.String(80), unique=False, nullable=False)
    device = db.Column(db.String(80), unique=False, nullable=False)
    fstype = db.Column(db.String(80), unique=False, nullable=False)
    mountpoint = db.Column(db.String(80), unique=False, nullable=False)
    total_gb = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<StaticDisk @{self.servername} (diskname:{self.diskname}, total_gb:{self.total_gb})>'


class StaticGPUModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    servername = db.Column(db.String(80), unique=True, nullable=False)
    device_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    uuid = db.Column(db.String(80), unique=False, nullable=False)
    total_gb = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<StaticGPU @{self.servername} (name:{self.name}, total_gb:{self.total_gb})>'

