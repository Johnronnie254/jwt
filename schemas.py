from marshmallow import fields, Schema


from users import User

class UserSchema(Schema):
    id = fields.String()
    username = fields.String()
    email = fields.String()

    
