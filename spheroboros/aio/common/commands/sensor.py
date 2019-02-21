#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x18-sensors.json
# Device ID:          0x18
# Device Name:        sensor
# Timestamp:          02/21/2019 @ 22:23:44.200688 (UTC)

from spheroboros.common.commands.sensor import CommandsEnum
from spheroboros.common.devices import DevicesEnum
from spheroboros.common.parameter import Parameter


async def set_sensor_streaming_mask(self, interval, packet_count, data_mask, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.set_sensor_streaming_mask,
        target,
        timeout,
        inputs=[
            Parameter(
                name='interval',
                data_type='uint16_t',
                index=0,
                value=interval,
                size=1
            ),
            Parameter(
                name='packetCount',
                data_type='uint8_t',
                index=1,
                value=packet_count,
                size=1
            ),
            Parameter(
                name='dataMask',
                data_type='uint32_t',
                index=2,
                value=data_mask,
                size=1
            ),
        ],
    )


async def get_sensor_streaming_mask(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.get_sensor_streaming_mask,
        target,
        timeout,
        outputs=[
            Parameter(
                name='interval',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter(
                name='packetCount',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='dataMask',
                data_type='uint32_t',
                index=2,
                size=1,
            ),
        ],
    )


async def on_sensor_streaming_data_notify(self, target, handler=None, timeout=None):
    await self._dal.on_command(
        DevicesEnum.sensor,
        CommandsEnum.sensor_streaming_data_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='sensorData',
                data_type='float',
                index=0,
                size=255
            ),
        ],
    )


async def get_encoder_counts(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.get_encoder_counts,
        target,
        timeout,
        outputs=[
            Parameter(
                name='encoderCounts',
                data_type='int16_t',
                index=0,
                size=2,
            ),
        ],
    )


async def get_euler_angles(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.get_euler_angles,
        target,
        timeout,
        outputs=[
            Parameter(
                name='pitch',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter(
                name='roll',
                data_type='float',
                index=1,
                size=1,
            ),
            Parameter(
                name='extendedRoll',
                data_type='float',
                index=2,
                size=1,
            ),
            Parameter(
                name='yaw',
                data_type='float',
                index=3,
                size=1,
            ),
        ],
    )


async def get_gyro_degrees_per_second(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.get_gyro_degrees_per_second,
        target,
        timeout,
        outputs=[
            Parameter(
                name='pitch',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter(
                name='roll',
                data_type='float',
                index=1,
                size=1,
            ),
            Parameter(
                name='yaw',
                data_type='float',
                index=2,
                size=1,
            ),
        ],
    )


async def set_extended_sensor_streaming_mask(self, data_mask, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.set_extended_sensor_streaming_mask,
        target,
        timeout,
        inputs=[
            Parameter(
                name='dataMask',
                data_type='uint32_t',
                index=0,
                value=data_mask,
                size=1
            ),
        ],
    )


async def get_extended_sensor_streaming_mask(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.get_extended_sensor_streaming_mask,
        target,
        timeout,
        outputs=[
            Parameter(
                name='dataMask',
                data_type='uint32_t',
                index=0,
                size=1,
            ),
        ],
    )


async def enable_gyro_max_notify(self, is_enabled, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.enable_gyro_max_notify,
        target,
        timeout,
        inputs=[
            Parameter(
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    )


async def on_gyro_max_notify(self, target, handler=None, timeout=None):
    await self._dal.on_command(
        DevicesEnum.sensor,
        CommandsEnum.gyro_max_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='flags',
                data_type='uint8_t',
                index=0,
                size=1
            ),
        ],
    )


async def configure_collision_detection(self, method, x_threshold, x_speed, y_threshold, y_speed, dead_time, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.configure_collision_detection,
        target,
        timeout,
        inputs=[
            Parameter(
                name='method',
                data_type='uint8_t',
                index=0,
                value=method,
                size=1
            ),
            Parameter(
                name='xThreshold',
                data_type='uint8_t',
                index=1,
                value=x_threshold,
                size=1
            ),
            Parameter(
                name='xSpeed',
                data_type='uint8_t',
                index=2,
                value=x_speed,
                size=1
            ),
            Parameter(
                name='yThreshold',
                data_type='uint8_t',
                index=3,
                value=y_threshold,
                size=1
            ),
            Parameter(
                name='ySpeed',
                data_type='uint8_t',
                index=4,
                value=y_speed,
                size=1
            ),
            Parameter(
                name='deadTime',
                data_type='uint8_t',
                index=5,
                value=dead_time,
                size=1
            ),
        ],
    )


async def on_collision_detected_notify(self, target, handler=None, timeout=None):
    await self._dal.on_command(
        DevicesEnum.sensor,
        CommandsEnum.collision_detected_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='accelerationX',
                data_type='uint16_t',
                index=0,
                size=1
            ),
            Parameter(
                name='accelerationY',
                data_type='uint16_t',
                index=1,
                size=1
            ),
            Parameter(
                name='accelerationZ',
                data_type='uint16_t',
                index=2,
                size=1
            ),
            Parameter(
                name='axis',
                data_type='uint8_t',
                index=3,
                size=1
            ),
            Parameter(
                name='powerX',
                data_type='uint16_t',
                index=4,
                size=1
            ),
            Parameter(
                name='powerY',
                data_type='uint16_t',
                index=5,
                size=1
            ),
            Parameter(
                name='speed',
                data_type='uint8_t',
                index=6,
                size=1
            ),
            Parameter(
                name='time',
                data_type='uint32_t',
                index=7,
                size=1
            ),
        ],
    )


async def get_bot_to_bot_infrared_readings(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.get_bot_to_bot_infrared_readings,
        target,
        timeout,
        outputs=[
            Parameter(
                name='sensorData',
                data_type='uint32_t',
                index=0,
                size=1,
            ),
        ],
    )


async def start_robot_to_robot_infrared_broadcasting(self, far_code, near_code, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.start_robot_to_robot_infrared_broadcasting,
        target,
        timeout,
        inputs=[
            Parameter(
                name='farCode',
                data_type='uint8_t',
                index=0,
                value=far_code,
                size=1
            ),
            Parameter(
                name='nearCode',
                data_type='uint8_t',
                index=1,
                value=near_code,
                size=1
            ),
        ],
    )


async def stop_robot_to_robot_infrared_broadcasting(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.stop_robot_to_robot_infrared_broadcasting,
        target,
        timeout,
    )


async def send_robot_to_robot_infrared_message(self, infrared_code, front_left_strength, front_right_strength, back_right_strength, back_left_strength, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.send_robot_to_robot_infrared_message,
        target,
        timeout,
        inputs=[
            Parameter(
                name='infraredCode',
                data_type='uint8_t',
                index=0,
                value=infrared_code,
                size=1
            ),
            Parameter(
                name='frontLeftStrength',
                data_type='uint8_t',
                index=1,
                value=front_left_strength,
                size=1
            ),
            Parameter(
                name='frontRightStrength',
                data_type='uint8_t',
                index=2,
                value=front_right_strength,
                size=1
            ),
            Parameter(
                name='backRightStrength',
                data_type='uint8_t',
                index=3,
                value=back_right_strength,
                size=1
            ),
            Parameter(
                name='backLeftStrength',
                data_type='uint8_t',
                index=4,
                value=back_left_strength,
                size=1
            ),
        ],
    )


async def listen_for_robot_to_robot_infrared_message(self, infrared_code, listen_duration, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.listen_for_robot_to_robot_infrared_message,
        target,
        timeout,
        inputs=[
            Parameter(
                name='infraredCode',
                data_type='uint8_t',
                index=0,
                value=infrared_code,
                size=1
            ),
            Parameter(
                name='listenDuration',
                data_type='uint32_t',
                index=1,
                value=listen_duration,
                size=1
            ),
        ],
    )


async def on_robot_to_robot_infrared_message_received_notify(self, target, handler=None, timeout=None):
    await self._dal.on_command(
        DevicesEnum.sensor,
        CommandsEnum.robot_to_robot_infrared_message_received_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='infraredCode',
                data_type='uint8_t',
                index=0,
                size=1
            ),
        ],
    )


async def get_ambient_light_sensor_value(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.get_ambient_light_sensor_value,
        target,
        timeout,
        outputs=[
            Parameter(
                name='ambientLightWhiteChannelValue',
                data_type='float',
                index=0,
                size=1,
            ),
        ],
    )


async def enable_color_detection_notification(self, enable, interval, minimum_confidence_threshold, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.enable_color_detection_notification,
        target,
        timeout,
        inputs=[
            Parameter(
                name='enable',
                data_type='bool',
                index=0,
                value=enable,
                size=1
            ),
            Parameter(
                name='interval',
                data_type='uint16_t',
                index=1,
                value=interval,
                size=1
            ),
            Parameter(
                name='minimumConfidenceThreshold',
                data_type='uint8_t',
                index=2,
                value=minimum_confidence_threshold,
                size=1
            ),
        ],
    )


async def on_color_detection_notify(self, target, handler=None, timeout=None):
    await self._dal.on_command(
        DevicesEnum.sensor,
        CommandsEnum.color_detection_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='red',
                data_type='uint8_t',
                index=0,
                size=1
            ),
            Parameter(
                name='green',
                data_type='uint8_t',
                index=1,
                size=1
            ),
            Parameter(
                name='blue',
                data_type='uint8_t',
                index=2,
                size=1
            ),
            Parameter(
                name='confidence',
                data_type='uint8_t',
                index=3,
                size=1
            ),
            Parameter(
                name='colorClassification',
                data_type='uint8_t',
                index=4,
                size=1
            ),
        ],
    )


async def get_current_detected_color_reading(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.get_current_detected_color_reading,
        target,
        timeout,
    )


async def enable_color_detection(self, enable, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.sensor,
        CommandsEnum.enable_color_detection,
        target,
        timeout,
        inputs=[
            Parameter(
                name='enable',
                data_type='bool',
                index=0,
                value=enable,
                size=1
            ),
        ],
    )
