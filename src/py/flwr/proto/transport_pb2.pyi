"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

global___Reason = Reason
class _Reason(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Reason.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    UNKNOWN = Reason.V(0)
    RECONNECT = Reason.V(1)
    POWER_DISCONNECTED = Reason.V(2)
    WIFI_UNAVAILABLE = Reason.V(3)
    ACK = Reason.V(4)
class Reason(metaclass=_Reason):
    V = typing.NewType('V', builtins.int)
UNKNOWN = Reason.V(0)
RECONNECT = Reason.V(1)
POWER_DISCONNECTED = Reason.V(2)
WIFI_UNAVAILABLE = Reason.V(3)
ACK = Reason.V(4)

class Parameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TENSORS_FIELD_NUMBER: builtins.int
    TENSOR_TYPE_FIELD_NUMBER: builtins.int
    tensors: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes] = ...
    tensor_type: typing.Text = ...

    def __init__(self,
        *,
        tensors : typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        tensor_type : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"tensor_type",b"tensor_type",u"tensors",b"tensors"]) -> None: ...
global___Parameters = Parameters

class ServerMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Reconnect(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        SECONDS_FIELD_NUMBER: builtins.int
        seconds: builtins.int = ...

        def __init__(self,
            *,
            seconds : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"seconds",b"seconds"]) -> None: ...

    class GetParameters(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

        def __init__(self,
            ) -> None: ...

    class FitIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...

            @property
            def value(self) -> global___Scalar: ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        PARAMETERS_FIELD_NUMBER: builtins.int
        CONFIG_FIELD_NUMBER: builtins.int

        @property
        def parameters(self) -> global___Parameters: ...

        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...

        def __init__(self,
            *,
            parameters : typing.Optional[global___Parameters] = ...,
            config : typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"config",b"config",u"parameters",b"parameters"]) -> None: ...

    class EvaluateIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...

            @property
            def value(self) -> global___Scalar: ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        PARAMETERS_FIELD_NUMBER: builtins.int
        CONFIG_FIELD_NUMBER: builtins.int

        @property
        def parameters(self) -> global___Parameters: ...

        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...

        def __init__(self,
            *,
            parameters : typing.Optional[global___Parameters] = ...,
            config : typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"config",b"config",u"parameters",b"parameters"]) -> None: ...

    class SecAggMsg(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class SetupParam(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            SECAGG_ID_FIELD_NUMBER: builtins.int
            SAMPLE_NUM_FIELD_NUMBER: builtins.int
            SHARE_NUM_FIELD_NUMBER: builtins.int
            THRESHOLD_FIELD_NUMBER: builtins.int
            secagg_id: builtins.int = ...
            sample_num: builtins.int = ...
            share_num: builtins.int = ...
            threshold: builtins.int = ...

            def __init__(self,
                *,
                secagg_id : builtins.int = ...,
                sample_num : builtins.int = ...,
                share_num : builtins.int = ...,
                threshold : builtins.int = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"sample_num",b"sample_num",u"secagg_id",b"secagg_id",u"share_num",b"share_num",u"threshold",b"threshold"]) -> None: ...

        class AskKeys(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

            def __init__(self,
                ) -> None: ...

        SETUP_PARAM_FIELD_NUMBER: builtins.int
        ASK_KEYS_FIELD_NUMBER: builtins.int

        @property
        def setup_param(self) -> global___ServerMessage.SecAggMsg.SetupParam: ...

        @property
        def ask_keys(self) -> global___ServerMessage.SecAggMsg.AskKeys: ...

        def __init__(self,
            *,
            setup_param : typing.Optional[global___ServerMessage.SecAggMsg.SetupParam] = ...,
            ask_keys : typing.Optional[global___ServerMessage.SecAggMsg.AskKeys] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"ask_keys",b"ask_keys",u"msg",b"msg",u"setup_param",b"setup_param"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"ask_keys",b"ask_keys",u"msg",b"msg",u"setup_param",b"setup_param"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal[u"msg",b"msg"]) -> typing_extensions.Literal["setup_param","ask_keys"]: ...

    RECONNECT_FIELD_NUMBER: builtins.int
    GET_PARAMETERS_FIELD_NUMBER: builtins.int
    FIT_INS_FIELD_NUMBER: builtins.int
    EVALUATE_INS_FIELD_NUMBER: builtins.int
    SEC_AGG_MSG_FIELD_NUMBER: builtins.int

    @property
    def reconnect(self) -> global___ServerMessage.Reconnect: ...

    @property
    def get_parameters(self) -> global___ServerMessage.GetParameters: ...

    @property
    def fit_ins(self) -> global___ServerMessage.FitIns: ...

    @property
    def evaluate_ins(self) -> global___ServerMessage.EvaluateIns: ...

    @property
    def sec_agg_msg(self) -> global___ServerMessage.SecAggMsg: ...

    def __init__(self,
        *,
        reconnect : typing.Optional[global___ServerMessage.Reconnect] = ...,
        get_parameters : typing.Optional[global___ServerMessage.GetParameters] = ...,
        fit_ins : typing.Optional[global___ServerMessage.FitIns] = ...,
        evaluate_ins : typing.Optional[global___ServerMessage.EvaluateIns] = ...,
        sec_agg_msg : typing.Optional[global___ServerMessage.SecAggMsg] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"evaluate_ins",b"evaluate_ins",u"fit_ins",b"fit_ins",u"get_parameters",b"get_parameters",u"msg",b"msg",u"reconnect",b"reconnect",u"sec_agg_msg",b"sec_agg_msg"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"evaluate_ins",b"evaluate_ins",u"fit_ins",b"fit_ins",u"get_parameters",b"get_parameters",u"msg",b"msg",u"reconnect",b"reconnect",u"sec_agg_msg",b"sec_agg_msg"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"msg",b"msg"]) -> typing_extensions.Literal["reconnect","get_parameters","fit_ins","evaluate_ins","sec_agg_msg"]: ...
global___ServerMessage = ServerMessage

class ClientMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Disconnect(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        REASON_FIELD_NUMBER: builtins.int
        reason: global___Reason.V = ...

        def __init__(self,
            *,
            reason : global___Reason.V = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"reason",b"reason"]) -> None: ...

    class ParametersRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        PARAMETERS_FIELD_NUMBER: builtins.int

        @property
        def parameters(self) -> global___Parameters: ...

        def __init__(self,
            *,
            parameters : typing.Optional[global___Parameters] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"parameters",b"parameters"]) -> None: ...

    class FitRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class MetricsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...

            @property
            def value(self) -> global___Scalar: ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        PARAMETERS_FIELD_NUMBER: builtins.int
        NUM_EXAMPLES_FIELD_NUMBER: builtins.int
        NUM_EXAMPLES_CEIL_FIELD_NUMBER: builtins.int
        FIT_DURATION_FIELD_NUMBER: builtins.int
        METRICS_FIELD_NUMBER: builtins.int
        num_examples: builtins.int = ...
        num_examples_ceil: builtins.int = ...
        fit_duration: builtins.float = ...

        @property
        def parameters(self) -> global___Parameters: ...

        @property
        def metrics(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...

        def __init__(self,
            *,
            parameters : typing.Optional[global___Parameters] = ...,
            num_examples : builtins.int = ...,
            num_examples_ceil : builtins.int = ...,
            fit_duration : builtins.float = ...,
            metrics : typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"fit_duration",b"fit_duration",u"metrics",b"metrics",u"num_examples",b"num_examples",u"num_examples_ceil",b"num_examples_ceil",u"parameters",b"parameters"]) -> None: ...

    class EvaluateRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class MetricsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...

            @property
            def value(self) -> global___Scalar: ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        NUM_EXAMPLES_FIELD_NUMBER: builtins.int
        LOSS_FIELD_NUMBER: builtins.int
        ACCURACY_FIELD_NUMBER: builtins.int
        METRICS_FIELD_NUMBER: builtins.int
        num_examples: builtins.int = ...
        loss: builtins.float = ...
        accuracy: builtins.float = ...

        @property
        def metrics(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...

        def __init__(self,
            *,
            num_examples : builtins.int = ...,
            loss : builtins.float = ...,
            accuracy : builtins.float = ...,
            metrics : typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"accuracy",b"accuracy",u"loss",b"loss",u"metrics",b"metrics",u"num_examples",b"num_examples"]) -> None: ...

    class SecAggRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class SetupParamRes(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

            def __init__(self,
                ) -> None: ...

        class AskKeysRes(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            PK1_FIELD_NUMBER: builtins.int
            PK2_FIELD_NUMBER: builtins.int
            pk1: builtins.bytes = ...
            pk2: builtins.bytes = ...

            def __init__(self,
                *,
                pk1 : builtins.bytes = ...,
                pk2 : builtins.bytes = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"pk1",b"pk1",u"pk2",b"pk2"]) -> None: ...

        class ErrorRes(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            ERROR_FIELD_NUMBER: builtins.int
            error: typing.Text = ...

            def __init__(self,
                *,
                error : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"error",b"error"]) -> None: ...

        SETUP_PARAM_RES_FIELD_NUMBER: builtins.int
        ASK_KEYS_RES_FIELD_NUMBER: builtins.int
        ERROR_RES_FIELD_NUMBER: builtins.int

        @property
        def setup_param_res(self) -> global___ClientMessage.SecAggRes.SetupParamRes: ...

        @property
        def ask_keys_res(self) -> global___ClientMessage.SecAggRes.AskKeysRes: ...

        @property
        def error_res(self) -> global___ClientMessage.SecAggRes.ErrorRes: ...

        def __init__(self,
            *,
            setup_param_res : typing.Optional[global___ClientMessage.SecAggRes.SetupParamRes] = ...,
            ask_keys_res : typing.Optional[global___ClientMessage.SecAggRes.AskKeysRes] = ...,
            error_res : typing.Optional[global___ClientMessage.SecAggRes.ErrorRes] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"ask_keys_res",b"ask_keys_res",u"error_res",b"error_res",u"msg",b"msg",u"setup_param_res",b"setup_param_res"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"ask_keys_res",b"ask_keys_res",u"error_res",b"error_res",u"msg",b"msg",u"setup_param_res",b"setup_param_res"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal[u"msg",b"msg"]) -> typing_extensions.Literal["setup_param_res","ask_keys_res","error_res"]: ...

    DISCONNECT_FIELD_NUMBER: builtins.int
    PARAMETERS_RES_FIELD_NUMBER: builtins.int
    FIT_RES_FIELD_NUMBER: builtins.int
    EVALUATE_RES_FIELD_NUMBER: builtins.int
    SEC_AGG_RES_FIELD_NUMBER: builtins.int

    @property
    def disconnect(self) -> global___ClientMessage.Disconnect: ...

    @property
    def parameters_res(self) -> global___ClientMessage.ParametersRes: ...

    @property
    def fit_res(self) -> global___ClientMessage.FitRes: ...

    @property
    def evaluate_res(self) -> global___ClientMessage.EvaluateRes: ...

    @property
    def sec_agg_res(self) -> global___ClientMessage.SecAggRes: ...

    def __init__(self,
        *,
        disconnect : typing.Optional[global___ClientMessage.Disconnect] = ...,
        parameters_res : typing.Optional[global___ClientMessage.ParametersRes] = ...,
        fit_res : typing.Optional[global___ClientMessage.FitRes] = ...,
        evaluate_res : typing.Optional[global___ClientMessage.EvaluateRes] = ...,
        sec_agg_res : typing.Optional[global___ClientMessage.SecAggRes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"disconnect",b"disconnect",u"evaluate_res",b"evaluate_res",u"fit_res",b"fit_res",u"msg",b"msg",u"parameters_res",b"parameters_res",u"sec_agg_res",b"sec_agg_res"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"disconnect",b"disconnect",u"evaluate_res",b"evaluate_res",u"fit_res",b"fit_res",u"msg",b"msg",u"parameters_res",b"parameters_res",u"sec_agg_res",b"sec_agg_res"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"msg",b"msg"]) -> typing_extensions.Literal["disconnect","parameters_res","fit_res","evaluate_res","sec_agg_res"]: ...
global___ClientMessage = ClientMessage

class Scalar(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DOUBLE_FIELD_NUMBER: builtins.int
    SINT64_FIELD_NUMBER: builtins.int
    BOOL_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    double: builtins.float = ...
    sint64: builtins.int = ...
    bool: builtins.bool = ...
    string: typing.Text = ...
    bytes: builtins.bytes = ...

    def __init__(self,
        *,
        double : builtins.float = ...,
        sint64 : builtins.int = ...,
        bool : builtins.bool = ...,
        string : typing.Text = ...,
        bytes : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"bool",b"bool",u"bytes",b"bytes",u"double",b"double",u"scalar",b"scalar",u"sint64",b"sint64",u"string",b"string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bool",b"bool",u"bytes",b"bytes",u"double",b"double",u"scalar",b"scalar",u"sint64",b"sint64",u"string",b"string"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"scalar",b"scalar"]) -> typing_extensions.Literal["double","sint64","bool","string","bytes"]: ...
global___Scalar = Scalar
