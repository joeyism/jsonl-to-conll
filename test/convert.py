import unittest
from snapshottest import TestCase
from jsonl_to_conll import convert

class TestConvert(TestCase):

  def setUp(self):
    self.input_data = {"id": 1, "text": "Ms. Elliott joined Cisco in April 2018. Ms. Elliott is a former Executive Vice President of Juniper Networks, Inc., where she served as EVP and Chief Customer Officer from March 2013 to February 2014, EVP and Chief Sales Officer from July 2011 to March 2013 and EVP, Strategic Alliances from June 2009 to July 2011. Before joining Juniper, Ms. Elliott held a series of senior executive positions with Microsoft Corporation from 2001-2008 including Corporate Vice President of Microsoft’s Industry Solutions Group, Worldwide Public Sector and North American Enterprise Sales organizations. Prior to joining Microsoft Corporation, Ms. Elliott spent 22 years at IBM Corporation, where she held several senior executive positions both in the U.S. and internationally. Since 2014 Ms. Elliott has served as a director on several public company boards including Whirlpool Corporation (since 2014), Bed Bath & Beyond, Inc. (2014-17), Imperva, Inc. (2015-18), Marvell Technology Group Ltd. (2017-18) and Mimecast Ltd. (2017-18), and during this period she also founded and led the development of Broadrooms.com, an informational resource for executive women who serve or want to serve on corporate boards in the U.S.", "meta": {}, "annotation_approver": None, "labels": [[0, 11, "PER"], [19, 24, "ORG"], [40, 51, "PER"], [92, 114, "ORG"], [267, 286, "ORG"], [331, 338, "ORG"], [606, 627, "ORG"], [855, 876, "ORG"], [891, 914, "ORG"], [926, 939, "ORG"], [951, 980, "ORG"], [995, 1008, "ORG"], [1087, 1101, "ORG"], [1203, 1206, "LOC"], [659, 674, "ORG"], [401, 422, "ORG"]]}

  def test_convert_successful(self):
    self.assertMatchSnapshot(convert.flatten(self.input_data))
