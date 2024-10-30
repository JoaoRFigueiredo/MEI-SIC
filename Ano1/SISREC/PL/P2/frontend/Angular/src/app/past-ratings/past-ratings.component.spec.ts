import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PastRatingsComponent } from './past-ratings.component';

describe('PastRatingsComponent', () => {
  let component: PastRatingsComponent;
  let fixture: ComponentFixture<PastRatingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PastRatingsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PastRatingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
