export interface Truck {
    id: string;
    plate: string;
    tare?: number;
    maxWeight?: number;
    batteryCapacity?: number;
    truckAutonomy?: number;
    chargeTime?: number;
    active?: boolean;
}