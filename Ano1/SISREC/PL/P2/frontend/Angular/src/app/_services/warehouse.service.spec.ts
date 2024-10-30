import { TestBed } from '@angular/core/testing';
import { HttpClient } from '@angular/common/http';
import { WarehouseService } from './warehouse.service';
import { of, throwError } from 'rxjs';
describe('WarehouseService', () => {
  let service: WarehouseService;
  let httpClientSpy: jasmine.SpyObj<HttpClient>;
  let WAREHOUSE = {
    id: "125",
      description: "Arouca",
      street: "Rua de Arouca",
      city: "Porto",
      country: "Portugal",
      latitude: 40.9321,
      longitude: 8.2451,
      altitude: 250.0
  }
  let WAREHOUSES =[
    {
      id: "123",
      description: "Arouca",
      street: "Rua de Arouca",
      city: "Porto",
      country: "Portugal",
      latitude: 40.9321,
      longitude: 8.2451,
      altitude: 250.0
    },
    {
      id: "124",
      description: "PORTO",
      street: "Rua de porto",
      city: "Lisboa",
      country: "Portugal",
      latitude: 41.9321,
      longitude: 7.2451,
      altitude: 450.0
    }];
  beforeEach(() => {
    httpClientSpy = jasmine.createSpyObj('HttpClient', ['get','post','put']);
    service = new WarehouseService(httpClientSpy);
  });

  describe('getWarehouses()', () => {
    it('should return expected warehouses when getWarehouse is called', (done: DoneFn)=>{
      httpClientSpy.get.and.returnValue(of(WAREHOUSES));
      service.getWarehouses().subscribe({
        next: (warehouses) => {
          expect(warehouses).toEqual(WAREHOUSES);
          done();
        },
        error: () => {},
      });
      expect(httpClientSpy.get).toHaveBeenCalledTimes(1);
    })
  });
  describe('getWarehouses()', () => {
    it('should throw an error when getWarehouse is called and the HTTP request fails', (done: DoneFn)=>{
      httpClientSpy.get.and.returnValue(throwError(new Error('HTTP request failed')));
      service.getWarehouses().subscribe({
        next: () => {},
        error: (error) => {
          expect(error).toEqual(new Error('HTTP request failed'));
          done();
        },
      });
      expect(httpClientSpy.get).toHaveBeenCalledTimes(1);
    })
  });
  describe('addWarehouse()', () => {
    it('should return expected warehouse when addWarehouse is called', (done: DoneFn)=>{
      httpClientSpy.post.and.returnValue(of(WAREHOUSE));
      service.addWarehouse(WAREHOUSE).subscribe({
        next: (warehouse) => {
          expect(warehouse).toEqual(WAREHOUSE);
          done();
        },
        error: () => {},
      });
      expect(httpClientSpy.post).toHaveBeenCalledTimes(1);
    })
  });
  describe('addWarehouse()', () => {
    it('should throw an error when getWarehouse is called and the HTTP request fails', (done: DoneFn)=>{
      httpClientSpy.get.and.returnValue(throwError(new Error('HTTP request failed')));
      service.getWarehouses().subscribe({
        next: () => {},
        error: (error) => {
          expect(error).toEqual(new Error('HTTP request failed'));
          done();
        },
      });
      expect(httpClientSpy.get).toHaveBeenCalledTimes(1);
    })
  });
});