import { HttpClient } from '@angular/common/http';
import { of, throwError } from 'rxjs'
import { TestBed } from '@angular/core/testing';

import { FleetService } from './fleet.service';
import { Truck } from '../_models/Truck';

describe('FleetService', () => {
  let service: FleetService;
  let httpClientSpy: jasmine.SpyObj<HttpClient>;
  let TRUCKS = [
    {
      id: "8a4e943c-f40d-4ffa-938b-c38a2acbdcea",
      plate: "AB-CD-00",
      tare: 21,
      maxWeight: 22,
      batteryCapacity: 32,
      truckAutonomy: 32,
      chargeTime: 23,
      active: true
    },
    {
      id: "0cd0578b-1aa0-450e-abdf-3170b168f432",
      plate: "AB-CD-01",
      tare: 1,
      maxWeight: 2,
      batteryCapacity: 5,
      truckAutonomy: 4,
      chargeTime: 2,
      active: true
    }];

  beforeEach(() => {
    httpClientSpy = jasmine.createSpyObj('HttpClient', ['get', 'patch', 'delete']);
    service = new FleetService(httpClientSpy);
  });

  describe('getTrucks()', () => {
    it('it should return expected trucks when called', (done: DoneFn) => {
      httpClientSpy.get.and.returnValue(of(TRUCKS));
      service.getTrucks().subscribe({
        next: (trucks) => {
          expect(trucks).toEqual(TRUCKS);
          done();
        },
        error: () => {
          done.fail;
        },
      });
      expect(httpClientSpy.get).toHaveBeenCalledTimes(1);
    });
    it('should handle a failed HTTP request', (done: DoneFn) => {
      httpClientSpy.get.and.returnValue(throwError(new Error('HTTP request failed')));
      service.getTrucks().subscribe({
        next: () => {},
        error: (error) => {
          expect(error).toEqual(new Error('HTTP request failed'));
          done();
        },
      });
      expect(httpClientSpy.get).toHaveBeenCalledTimes(1);
    });
  })

  describe('patchTruck()', () => {
    it('should update a truck', () => {
      const mockTruck: Truck = { id: '8a4e943c-f40d-4ffa-938b-c38a2acbdcea', plate: 'AB-CD-00', active: true };
      const mockInfo = { id: '8a4e943c-f40d-4ffa-938b-c38a2acbdcea', plate: 'AB-CD-00', active: false };
  
      httpClientSpy.patch.and.returnValue(of(mockTruck));
      service.patchTruck(mockInfo).subscribe(truck => {
        expect(truck).toEqual(mockTruck);
      });
      expect(httpClientSpy.patch).toHaveBeenCalledTimes(1);
    });
    
    it('should handle error when updating a truck', () => {
      const mockUpdate = { id: '8a4e943c-f40d-4ffa-938b-c38a2acbdcea', plate: 'AB-CD-00', active: false };
      const error = new Error('Error updating truck');
  
      httpClientSpy.patch.and.returnValue(throwError(error));
      service.patchTruck(mockUpdate).subscribe(
        () => { fail('Expected an error, but the call succeeded'); },
        (err) => { expect(err).toEqual(error); }
      );
      expect(httpClientSpy.patch).toHaveBeenCalledTimes(1);
    });

    it('should handle error when updating a truck with missing plate', () => {
      const mockUpdate = { id: '8a4e943c-f40d-4ffa-938b-c38a2acbdcea', active: false };
      const error = new Error('Error updating truck: plate is required');
  
      httpClientSpy.patch.and.returnValue(throwError(error));
      service.patchTruck(mockUpdate).subscribe(
        () => { fail('Expected an error, but the call succeeded'); },
        (err) => { expect(err).toEqual(error); }
      );
      expect(httpClientSpy.patch).toHaveBeenCalledTimes(1);
    });
  }) 

  describe('deleteTruck()', () => {
    it('should delete a truck', () => {
      const mockTruck: Truck = { id: '8a4e943c-f40d-4ffa-938b-c38a2acbdcea', plate: 'AB-CD-23', active: true };
      const mockId = '8a4e943c-f40d-4ffa-938b-c38a2acbdcea';
  
      httpClientSpy.delete.and.returnValue(of(mockTruck));
      service.deleteTruck(mockId).subscribe(truck => {
        expect(truck).toEqual(mockTruck);
      });
      expect(httpClientSpy.delete).toHaveBeenCalledTimes(1);
    });

    it('should handle error when deleting a truck', () => {
      const mockId = '8a4e943c-f40d-4ffa-938b-c38a2acbdcea';
      const error = new Error('Error deleting truck');
  
      httpClientSpy.delete.and.returnValue(throwError(error));
      service.deleteTruck(mockId).subscribe(
        () => { fail('Expected an error, but the call succeeded'); },
        (err) => { expect(err).toEqual(error); }
      );
      expect(httpClientSpy.delete).toHaveBeenCalledTimes(1);
    });

    it('should handle error when deleting a truck with empty id', () => {
      const error = new Error('Error deleting truck: ID is required');
  
      httpClientSpy.delete.and.returnValue(throwError(error));
      service.deleteTruck('').subscribe(
        () => { fail('Expected an error, but the call succeeded'); },
        (err) => { expect(err).toEqual(error); }
      );
      expect(httpClientSpy.delete).toHaveBeenCalledTimes(1);
    });
  })
});