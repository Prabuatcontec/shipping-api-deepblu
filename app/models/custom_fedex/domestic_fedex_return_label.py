import json
import jsonpickle
from json import JSONEncoder


class Student(object):
    def __init__(self, rollNumber, name, marks):
        self.rollNumber = rollNumber
        self.name = name
        self.marks = marks


class Marks(object):
    def __init__(self, english, geometry):
        self.english = english
        self.geometry = geometry


class LabelResponseOptions(object):
    def __init__(self, labelResponseOptions):
        self.labelResponseOptions = labelResponseOptions


class RequestedShipment(object):
    def __init__(self, shipper, recipients, shipDatestamp, serviceType, packagingType, pickupType, blockInsightVisibility,
                 shippingChargesPayment, shipmentSpecialServices, labelSpecification, requestedPackageLineItems):
        self.shipper = shipper
        self.recipients = recipients
        self.shipDatestamp = shipDatestamp
        self.serviceType = serviceType
        self.packagingType = packagingType
        self.pickupType = pickupType
        self.blockInsightVisibility = blockInsightVisibility
        self.shippingChargesPayment = shippingChargesPayment
        self.shipmentSpecialServices = shipmentSpecialServices
        self.labelSpecification = labelSpecification
        self.requestedPackageLineItems = requestedPackageLineItems


class Shipper(object):
    def __init__(self, contact, address):
        self.contact = contact
        self.address = address


class Recipients(object):
    def __init__(self, contact, address):
        self.contact = contact
        self.address = address


class Contact(object):
    def __init__(self, personName, phoneNumber, companyName):
        self.personName = personName
        self.phoneNumber = phoneNumber
        self.companyName = companyName


class Address(object):
    def __init__(self, streetLines, city, stateOrProvinceCode, postalCode, countryCode):
        self.streetLines = streetLines
        self.city = city
        self.stateOrProvinceCode = stateOrProvinceCode
        self.postalCode = postalCode
        self.countryCode = countryCode


class ShippingChargesPayment(object):
    def __init__(self, paymentType):
        self.paymentType = paymentType

class ShipmentSpecialServices(object):
    def __init__(self, specialServiceTypes, returnShipmentDetail):
        self.specialServiceTypes = specialServiceTypes
        self.returnShipmentDetail = returnShipmentDetail

class ReturnShipmentDetail(object):
    def __init__(self, returnType):
        self.returnType = returnType

class LabelSpecification(object):
    def __init__(self, imageType, labelStockType):
        self.imageType = imageType
        self.labelStockType = labelStockType
    
 
