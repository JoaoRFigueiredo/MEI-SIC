import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BoardEmployeeComponent } from './board-employee.component';

describe('BoardEmployeeComponent', () => {
  let component: BoardEmployeeComponent;
  let fixture: ComponentFixture<BoardEmployeeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BoardEmployeeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BoardEmployeeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
