## 📱 Android Performance Optimization: MediaPipe & CameraX

본 문서는 실시간 제스처 인식 애플리케이션 개발 중 발생한 메모리 누수 및 시스템 프리징 현상을 Logcat 데이터를 기반으로 분석하고 해결한 과정을 기록한 회고록입니다.

```
# 안드로이드 스튜디오 Logcat 명령어
package:com.buulgyeonE202.frontend (tag:GestureHelper | tag:PoseHelper | tag:Choreographer | "GC" | "MemoryCheck")

# 테스트 시간: 5min
```

---

### 1. Before: 기존 코드의 문제점 분석

기존 코드에서는 비동기 처리와 자원 해제 미흡으로 인해 시스템이 정상 구동 불가능한 상태였습니다.

* **치명적인 시스템 프리징**: 가비지 컬렉터(GC)가 메모리를 정리하는 동안 앱이 최대 **7.218초(7,218ms)** 동안 완전히 멈추는 'Stop-the-world' 현상이 발생
* **심각한 프레임 유실**: Choreographer를 통해 확인된 결과, 한 번에 **478개 이상의 프레임**이 유실되어 화면 트래킹이 불가능한 수준
* **AI 엔진 가동 중단**: 멀티스레드 환경에서 분석 프레임의 순서가 뒤섞이며, MediaPipe 엔진이 이전 프레임보다 과거의 타임스탬프를 수신하여 분석을 스스로 중단
* **메모리 고갈(LOS)**: 비트맵 객체가 명시적으로 해제되지 않아 대형 객체 공간(LOS)에 쓰레기 데이터가 적체되어 시스템 마비를 초래

```
# 로그 근거 (Logcat_rawdata_before.txt)
# (7.2초간 앱 정지)
Background concurrent copying GC ... paused 7.218s

# (화면이 거의 멈춤)
Choreographer: Skipped 478 frames!

# (AI 분석 포기)
GestureHelper: ... smaller than the previous timestamp
```

---

### 2. after_first: 성능 최적화 및 해결 방법

명시적 자원 관리와 AI 분석 파이프라인의 구조 개선을 통해 문제를 해결했습니다.

* **자원 해제 로직 구현**: `imageProxy.close()`와 비트맵 `recycle()`을 `finally` 블록에서 강제로 수행하여 대형 객체 메모리를 즉시 시스템에 반환
* **지연 시간 획기적 단축**: GC 일시 정지 시간이 **95us ~ 393us(마이크로초)** 단위로 줄어들어, 사용자가 체감할 수 없는 수준(기존 대비 약 14,000배 개선)으로 안정화
* **메모리 가용성 확보**: 대형 객체(LOS)를 초당 최대 **32MB**씩 실시간으로 회수하며, 장시간 구동 시에도 힙 메모리의 약 50%를 가용 상태로 일정하게 유지
* **데이터 정렬 보장**: 분석 Executor를 단일 스레드로 변경하여 타임스탬프 역전 현상을 원천 차단하고 AI 인식의 연속성을 확보

```
# 로그 근거 (Logcat_rawdata_before.txt)
# (마이크로초 단위의 일시 정지)
paused 393us, 384us, paused 95us

# (대형 객체를 즉시 회수하여 비워냄)
freed 28(32MB) LOS objects

# AI 엔진 에러(Timestamp smaller than...) 0건
```

---

### 📊 성능 개선 비교 (Before vs After)

| 비교 지표 | Before (Legacy) | After (Optimized) | 개선 결과 |
| :--- | :--- | :--- | :--- |
| **GC Pause Time** | **7,218ms** | **0.5ms (549us)** | **약 14,000배 개선** |
| **LOS 메모리 회수** | 적체 후 폭발적 GC 발생 | 실시간/주기적 자원 회수 | **안정적 유지** |
| **AI 엔진 에러** | Timestamp 충돌 다수 발생 | **에러 발생 0건** | **완전 해결** |
| **프레임 드랍** | 초당 수백 프레임 유실 | 유실 거의 없음 (60fps 유지) | **쾌적한 UX** |

---

### 💡 기술적 회고
안드로이드에서 비트맵과 같은 고용량 데이터를 다룰 때, JVM의 가비지 컬렉션에만 의존하는 것은 시스템 전체의 중단을 야기할 수 있음을 확인했습니다. 명시적인 자원 해제의 중요성과 실시간 AI 모델에 최적화된 스레딩 모델 설계가 애플리케이션의 생존성과 직결됨을 로그 데이터 수치로 입증한 소중한 경험이었다.