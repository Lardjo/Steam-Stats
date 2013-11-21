#!/usr/bin/env python3

from bson import ObjectId
from .base import BaseHandler


class DiretideHandler(BaseHandler):
    def get(self):
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})
        diretide = self.application.db["matches"].find({"game_mode": 7}).sort("match_id", -1).limit(20)
        self.render("diretide.html", session=session, diretide=diretide)