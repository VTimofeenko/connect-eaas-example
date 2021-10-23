# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Vladimir Timofeenko
# All rights reserved.
#
from connect.eaas.extension import (
    Extension,
    ProcessingResponse,
    ValidationResponse,
)


class DemoProjectExtension(Extension):

    async def process_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    async def validate_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    async def validate_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    