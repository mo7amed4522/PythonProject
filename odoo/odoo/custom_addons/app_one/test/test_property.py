from odoo.tests.common import TransactionCase


class TestProperty(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestProperty, self).setUp()

        self.property_01_record = self.env['property'].create({
            'ref':'MM0003',
            'name':'property test1',
            'expire_price':1000,
            'description':'description test1',

        })

    def test_01_property_values(self):
        property_id = self.property_01_record
        self.assertRecordValues(property_id, [{
            'ref':'MM0003',
            'name':'property test1',
            'expire_price':1000,
            'description':'description test1',
        }])