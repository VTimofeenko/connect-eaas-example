# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Vladimir Timofeenko
# All rights reserved.
#
import pytest

from connect_ext.extension import DemoProjectExtension


@pytest.mark.asyncio
async def test_process_asset_purchase_request(
    async_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = await async_client_factory(responses)
    ext = DemoProjectExtension(client, logger, config)
    result = await ext.process_asset_purchase_request(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_validate_asset_purchase_request(
    async_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = await async_client_factory(responses)
    ext = DemoProjectExtension(client, logger, config)
    result = await ext.validate_asset_purchase_request(request)
    assert result.status == 'success'
    assert result.data == request


@pytest.mark.asyncio
async def test_validate_asset_change_request(
    async_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = await async_client_factory(responses)
    ext = DemoProjectExtension(client, logger, config)
    result = await ext.validate_asset_change_request(request)
    assert result.status == 'success'
    assert result.data == request
