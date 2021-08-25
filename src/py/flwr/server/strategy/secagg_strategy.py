from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from flwr.common.typing import FitIns, Parameters
from flwr.server.client_manager import ClientManager
from flwr.server.client_proxy import ClientProxy


class SecAggStrategy(ABC):
    @abstractmethod
    def get_sec_agg_param(self) -> Dict[str, int]:
        '''Produce a dictionary storing parameters for the secure aggregation protocol
        min_num: Minimum number of clients to be available at the end of protocol
        min_frac: Minimum fraction of clients available with respect to sampled number at the end of protocol
        share_num: Number of shares to be generated for secret
        threshold: Number of shares needed to reconstruct secret
        clipping_range: Range of weight vector initially
        target_range: Range of weight vector after quantization
        mod_range: Field of cryptographic primitives
        max_weights_factor: maximum weights factor mulitplied on weights vector
        timeout: not used, but timeout for gRPC in the future

        Note: do not use secagg_id or sample_num, as it will be used overwritten on server side'''