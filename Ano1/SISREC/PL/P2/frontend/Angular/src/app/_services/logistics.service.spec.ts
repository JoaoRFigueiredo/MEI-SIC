import { TestBed } from '@angular/core/testing';
import { HttpClient } from '@angular/common/http';
import { LogisticsService } from './logistics.service';
import { of, throwError } from 'rxjs';
describe('LogisticsService', () => {
  let service: LogisticsService;
  let httpClientSpy: jasmine.SpyObj<HttpClient>;
  let PATH = {
    warehouseDeparture: 4,
    warehouseDestination: 5,
    distance:6,
    travelTime:7,
    energyNecessary:8,
    additionalTime:9
  }
  let PATHS =[
    {
      warehouseDeparture: 1,
      warehouseDestination: 2,
      distance:3,
      travelTime:4,
      energyNecessary:5,
      additionalTime:6
      }, {
      warehouseDeparture: 10,
      warehouseDestination: 12,
      distance:31,
      travelTime:42,
      energyNecessary:53,
      additionalTime:64
}];
  beforeEach(() => {
    httpClientSpy = jasmine.createSpyObj('HttpClient', ['get','post','put']);
    service = new LogisticsService(httpClientSpy);
  });

  describe('getPaths()', () => {
    it('should return expected paths when getPath is called', (done: DoneFn)=>{
      httpClientSpy.get.and.returnValue(of(PATHS));
      service.getPaths().subscribe({
        next: (Paths) => {
          expect(Paths).toEqual(PATHS);
          done();
        },
        error: () => {},
      });
      expect(httpClientSpy.get).toHaveBeenCalledTimes(1);
    })
  });
  describe('getPaths()', () => {
    it('should throw an error when getPaths is called and the HTTP request fails', (done: DoneFn)=>{
      httpClientSpy.get.and.returnValue(throwError(new Error('HTTP request failed')));
      service.getPaths().subscribe({
        next: () => {},
        error: (error) => {
          expect(error).toEqual(new Error('HTTP request failed'));
          done();
        },
      });
      expect(httpClientSpy.get).toHaveBeenCalledTimes(1);
    })
  });
  describe('postPath()', () => {
    it('should return expected path when postPath is called', (done: DoneFn)=>{
      httpClientSpy.post.and.returnValue(of(PATH));
      service.postPath(PATH).subscribe({
        next: (path) => {
          expect(path).toEqual(PATH);
          done();
        },
        error: () => {},
      });
      expect(httpClientSpy.post).toHaveBeenCalledTimes(1);
    })
  });
  describe('getPackaging()', () => {
    it('should throw an error when getPaths is called and the HTTP request fails', (done: DoneFn)=>{
      httpClientSpy.get.and.returnValue(throwError(new Error('HTTP request failed')));
      service.getPaths().subscribe({
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