import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonalizedRecommendationsComponent } from './personalized-recommendations.component';

describe('PersonalizedRecommendationsComponent', () => {
  let component: PersonalizedRecommendationsComponent;
  let fixture: ComponentFixture<PersonalizedRecommendationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PersonalizedRecommendationsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PersonalizedRecommendationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
