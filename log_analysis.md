# 사고 원인 분석 보고서

## 1. 개요
본 보고서는 `mission_computer_main.log` 파일의 로그 기록을 기반으로 로켓 임무 중 발생한 사고의 원인을 분석한 결과를 정리한 문서입니다.

## 2. 로그 요약
- 2023-08-27 10:00:00 ~ 11:30:00: 로켓의 정상적인 발사, 궤도 진입, 위성 분리, 재진입 및 착륙 과정이 순차적으로 기록됨.
- 2023-08-27 11:35:00: "Oxygen tank unstable."(산소 탱크 불안정) 메시지 기록
- 2023-08-27 11:40:00: "Oxygen tank explosion."(산소 탱크 폭발) 메시지 기록
- 2023-08-27 12:00:00: "Center and mission control systems powered down."(시스템 종료) 메시지로 로그 종료

## 3. 사고 발생 시점 및 경과
- 11:28:00: "Touchdown confirmed. Rocket safely landed." (로켓 안전 착륙)
- 11:30:00: "Mission completed successfully. Recovery team dispatched." (임무 완료, 회수팀 출동)
- 11:35:00: "Oxygen tank unstable." (산소 탱크 불안정)
- 11:40:00: "Oxygen tank explosion." (산소 탱크 폭발)
- 12:00:00: "Center and mission control systems powered down." (시스템 종료)

## 4. 사고 원인 추론
- 로켓이 착륙한 후(11:28~11:30) 임무가 성공적으로 종료된 것으로 기록됨.
- 그러나 착륙 후 약 5분 뒤(11:35)에 산소 탱크의 불안정이 감지되었고, 5분 후(11:40)에 산소 탱크가 폭발함.
- 임무 중에는 산소 탱크 관련 이상 징후가 전혀 없었으나, 착륙 이후에 문제가 발생함.
- 회수팀이 출동한 시점(11:30)과 사고 발생 시점(11:35~11:40)이 근접함.

### 주요 추론
- 산소 탱크의 불안정 및 폭발은 로켓이 착륙한 이후, 회수 과정 또는 외부 환경 변화에 의해 유발된 것으로 보임.
- 회수팀의 접근, 외부 충격, 온도 변화, 잔여 연료/산소의 관리 미흡 등이 원인일 수 있음.
- 시스템은 폭발 이후 20분 뒤(12:00)에 완전히 종료됨.

## 5. 결론 및 권고 사항
- 사고는 임무 종료 후, 회수 단계에서 발생한 2차적 사고로 판단됨.
- 회수 절차 중 산소 탱크의 상태 점검 및 안전 조치 강화 필요
- 착륙 후 잔여 산소 및 연료의 안전한 처리 매뉴얼 마련 필요
- 회수팀의 접근 전, 원격으로 탱크 상태를 재점검하는 절차 도입 권고

## 6. 참고 로그
```
2023-08-27 11:30:00,INFO,Mission completed successfully. Recovery team dispatched.
2023-08-27 11:35:00,INFO,Oxygen tank unstable.
2023-08-27 11:40:00,INFO,Oxygen tank explosion.
2023-08-27 12:00:00,INFO,Center and mission control systems powered down.
```
