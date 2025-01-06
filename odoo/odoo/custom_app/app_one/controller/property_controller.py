import math

from PIL.ImageChops import offset

from odoo import  http
from odoo.http import request
import  json
from urllib.parse import parse_qs

class PropertyApi(http.Controller):
    @http.route('/v1/api/property', type='http', auth='none', methods=['POST'], csrf=False)
    def post_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get('name') :
            return request.make_json_response({
                "status": 400,
                "message": "Property not created Name is required",
                "data": "No data found"
            },status=400)
        elif not vals.get('description') :
            return request.make_json_response({
                "status": 400,
                "message": "Property not created Description is required",
                "data": "No data found"
            },status=400)
        try:
            res = request.env['property'].sudo().create(vals)
            if res:
                return request.make_json_response({
                    "status": 200,
                    "message": "Property created successfully",
                    "data": res
                },status=200)
        except Exception as error:
            return request.make_json_response({
                "status": 400,
                "message": "Property not created",
                "data": str(error)
            },status=400)

    @http.route('/v1/api/property/json', type='json', auth='none', methods=['POST'], csrf=False)
    def post_property_json(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['property'].sudo().create(vals)
        if res:
            return [{
                "status": 200,
                "message": "Property created successfully",
                "data": res
            }]

    @http.route('/v1/api/property/<int:property_id>', type='http', auth='none', methods=['PUT'], csrf=False)
    def update_property(self, property_id):
        try:
            property_id = request.env['property'].sudo().search([('id','=',property_id)])
            if not property_id:
                return request.make_json_response({
                    "status": 400,
                    "message": "Property ID Not EXIST",
                    "data": "No data found"
                },status=400)
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            property_id.write(vals)
            return request.make_json_response({
                "status": 200,
                "message": "Property updated successfully",
                "data": property_id
            },status=200)
        except Exception as error:
            return request.make_json_response({
                "status": 400,
                "message": "Property error update",
                "data": str(error)
            },status=400)

    @http.route('/v1/api/property/<int:property_id>', type='http', auth='none', methods=['GET'], csrf=False)
    def get_property(self, property_id):
        try:
            property_id = request.env['property'].sudo().search([('id','=',property_id)])
            if not property_id:
                return request.make_json_response({
                    "status": 400,
                    "message": "Property ID Not EXIST",
                    "data": "No data found"
                },status=400)
            return request.make_json_response({
                "status": 200,
                "message": "Property get successfully",
                "data": property_id
            },status=200)
        except Exception as error:
            return request.make_json_response({
                "status": 400,
                "message": "Property error get",
                "data": str(error)
            },status=400)
    @http.route('/v1/api/property/<int:property_id>', type='http', auth='none', methods=['DELETE'], csrf=False)
    def delete_property(self, property_id):
        try:
            property_id = request.env['property'].sudo().search([('id','=',property_id)])
            if not property_id:
                return request.make_json_response({
                    "status": 400,
                    "message": "Property ID Not EXIST",
                    "data": "No data found"
                },status=400)
            property_id.unlink()
            return request.make_json_response({
                "status": 200,
                "message": "Property deleted successfully",
                "data": property_id
            },status=200)
        except Exception as error:
            return request.make_json_response({
                "status": 400,
                "message": "Property error delete",
                "data": str(error)
            },status=400)

    @http.route('/v1/api/properties', type='http', auth='none', methods=['GET'], csrf=False)
    def get_property_list(self):
        try:
            params = parse_qs(request.httprequest.query_string.decode('utf-8'))
            property_domain=[]
            page =offse = None
            limit = 5
            if params:
                if params.get('limit'):
                    limit = int(params.get('limit')[0])
                if params.get('page'):
                    page = int(params.get('page')[0])

            if page:
                offse = (page * limit) - limit
            if params.get('state'):
                property_domain +=[('state','=',params.get('state')[0])]
            property_ids = request.env['property'].sudo().search(property_domain, offset=offse, limit=limit, order='id DESC')
            property_count = request.env['property'].sudo().search_count(property_domain)
            pagination_info={
                'page':page if page else 1,
                'limit':limit,
                'pages':math.ceil(property_count/limit) if limit else 1,
                'count':property_count,
            }
            if not property_ids:
                return request.make_json_response({
                    "status": 400,
                    "message": "Property Not EXIST",
                    "data": "No data found"
                },status=400)
            return request.make_json_response({
                "status": 200,
                "message": "Property get successfully",
                'pagination':pagination_info,
                "data": [{
                    "id":property_id.id,
                    "name":property_id.name,
                    "ref":property_id.ref,
                    "description":property_id.description,
                    "is_late":property_id.is_late,
                    "expected_date":property_id.expected_date,
                    "expire_price":property_id.expire_price,
                    "diff":property_id.diff,
                    "state":property_id.state,
                    "owner_id":property_id.owner_id,
                    "postcode":property_id.postcode,
                    "area_oration":property_id.area_oration,
                    "tag_ids":property_id.tag_ids,
                }for property_id in property_ids]},status=200)
        except Exception as error:
            return request.make_json_response({
                "status": 400,
                "message": "Property error get",
                "data": str(error)
            },status=400)