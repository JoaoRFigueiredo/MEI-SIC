import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisableEmployeeComponent } from './disable-employee.component';

describe('DisableEmployeeComponent', () => {
  let component: DisableEmployeeComponent;
  let fixture: ComponentFixture<DisableEmployeeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DisableEmployeeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisableEmployeeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
