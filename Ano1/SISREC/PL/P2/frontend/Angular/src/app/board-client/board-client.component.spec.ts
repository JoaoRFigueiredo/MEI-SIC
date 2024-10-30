import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BoardClientComponent } from './board-client.component';

describe('BoardClientComponent', () => {
  let component: BoardClientComponent;
  let fixture: ComponentFixture<BoardClientComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BoardClientComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BoardClientComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
