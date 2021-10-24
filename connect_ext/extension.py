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


class Reasons:
    NOT_ENOUGH_ITEMS = "Not all required items were ordered"
    WRONG_QUANTITY = "Quantity of items is not equal"


class DemoProjectExtension(Extension):
    async def process_asset_purchase_request(self, request):
        """This is a demo middleware for validation.

        It reacts to incoming pending purchase requests and checks the following:
            * That multiple items were ordered (e.g. not just a device and not just a subscription)
            * That the quantities of ordered items are the same (e.g. that someone did not purchase 3 items and 5
            subscriptions)

        If a check is failed, corresponding message is recorded in the Conversation object of the request and the
        request is marked as failed.

        If all checks pass, the request is approved.

        """

        async def fail_request(reason: str):
            """Helper function that fails a request and logs it"""
            self.logger.warning(f"Failed request {request['id']}. Reason: {reason}")
            await self.client.requests[request["id"]]("fail").post({"reason": reason})

        self.logger.info(f"Obtained purchase request with id {request['id']}")

        self.logger.info("Checking items")
        items_list = request["asset"]["items"]

        # Fail if not all items were ordered
        if len(items_list) < 2:
            self.logger.warning("Amount of items is lower than threshold")

            # fail the request in Connect portal
            await fail_request(Reasons.NOT_ENOUGH_ITEMS)
            # need to return here, since this is the end of the logic
            return ProcessingResponse.done()

        # trivial check for quantity - get the quantity of the first item
        # and fail if not all items have the same quantity
        target_qty = items_list[0]["quantity"]

        if not all((item["quantity"] == target_qty for item in items_list[1:])):
            self.logger.warning(f"Quantity of items is lower than threshold of {target_qty}")
            await fail_request(Reasons.WRONG_QUANTITY)
        else:
            await self.client.requests[request["id"]]("approve").post({"template_id": "TL-906-236-964"})

        # note, "done" in this context means - done in the business logic sense of the extension
        # i.e. the extension followed an expected path, no exceptions raied.
        return ProcessingResponse.done()

    async def validate_asset_purchase_request(self, request):
        self.logger.info(f"Obtained validation purchase request with id {request['id']}")
        return ValidationResponse.done(request)

    async def validate_asset_change_request(self, request):
        self.logger.info(f"Obtained validation change request with id {request['id']}")
        return ValidationResponse.done(request)
