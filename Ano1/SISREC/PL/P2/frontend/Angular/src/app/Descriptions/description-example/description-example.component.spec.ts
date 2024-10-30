import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DescriptionExampleComponent } from './description-example.component';

describe('DescriptionExampleComponent', () => {
  let component: DescriptionExampleComponent;
  let fixture: ComponentFixture<DescriptionExampleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DescriptionExampleComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DescriptionExampleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
