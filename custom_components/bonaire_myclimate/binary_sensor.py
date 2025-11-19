from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorDeviceClass,
)

from .const import (
    DEVICE_MANUFACTURER, DEVICE_MODEL, SENSOR_NAME, DOMAIN,
)

async def async_setup_entry(hass, config_entry, async_add_entities):
    hub = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([HubAvailableBinarySensor(hub)])

class HubAvailableBinarySensor(BinarySensorEntity):
    def __init__(self, hub):
        self._hub = hub
        self._attr_name = "Bonaire MyClimate Available"
        self._attr_device_class = BinarySensorDeviceClass.CONNECTIVITY

    @property
    def unique_id(self):
        return SENSOR_NAME

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, SENSOR_NAME)},
            "name": SENSOR_NAME,
            "model": DEVICE_MODEL,
            "manufacturer": DEVICE_MANUFACTURER,
        }

    @property
    def is_on(self):
        return self._hub.available

    @property
    def available(self):
        return self._hub.available

    def update(self):
        pass

