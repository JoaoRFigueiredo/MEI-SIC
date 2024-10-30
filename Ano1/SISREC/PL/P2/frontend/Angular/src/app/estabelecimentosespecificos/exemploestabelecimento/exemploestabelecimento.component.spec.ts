import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExemploestabelecimentoComponent } from './exemploestabelecimento.component';

describe('ExemploestabelecimentoComponent', () => {
  let component: ExemploestabelecimentoComponent;
  let fixture: ComponentFixture<ExemploestabelecimentoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ExemploestabelecimentoComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExemploestabelecimentoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
