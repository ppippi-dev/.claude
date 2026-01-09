---
description: "Git 커밋, 푸시, PR 작업 수행 (Conventional Commits)"
---

현재까지 작업한 내용을 커밋하고 푸시합니다.

## Commit Message Format (Conventional Commits)

```
<type>(<scope>): <description>

[optional body]
```

### Types

| Type | Description |
|------|-------------|
| feat | 새로운 기능 추가 |
| fix | 버그 수정 |
| docs | 문서 변경 |
| style | 코드 포맷팅 (기능 변경 없음) |
| refactor | 리팩토링 (기능/버그 수정 아님) |
| test | 테스트 추가/수정 |
| chore | 빌드, 설정 등 기타 변경 |

### Examples

```bash
# Good
git commit -m "feat(auth): add JWT token validation"
git commit -m "fix(api): resolve null pointer in payment flow"
git commit -m "docs(readme): update installation guide"

# Bad - avoid these patterns
git commit -m "fix stuff"
git commit -m "WIP"
git commit -m "Changes"
```

## 수행 단계

1. **브랜치 생성**
   - 현재 브랜치 확인: `git branch --show-current`
   - main/master에 있다면 새 브랜치 생성 필수
   - `git checkout -b <type>/<short-description>`
   - 변경사항 분석 후 적절한 브랜치명 결정

2. **현재 변경사항 확인**
   - `git status`로 staged/unstaged 변경사항 확인
   - `git diff`로 각 파일의 변경 내용 파악

3. **Pre-Commit 검사**
   - 시크릿 검사: API 키, 비밀번호, 토큰 등 민감 정보 확인
   - 디버그 코드 제거: console.log, print 등 제거
   - 파일 끝 줄바꿈 검증: 모든 파일이 newline으로 끝나는지 확인
   - Python 프로젝트: `uv run pre-commit run` 실행

4. **커밋**
   - `git add [관련 파일들]`
   - Conventional Commits 형식으로 커밋 메시지 작성
   - `git commit -m "type(scope): 설명"`

5. **브랜치에 푸시**
   - `git push -u origin <branch>`

6. **완료 확인**
   - `git log --oneline -5`으로 커밋 이력 확인
   - `git status`로 상태 확인

## Branch Naming

```
<type>/<ticket-id>-<short-description>
```

| Type | Purpose |
|------|---------|
| feature/ | 새 기능 개발 |
| bugfix/ | 버그 수정 |
| hotfix/ | 긴급 수정 (production) |
| release/ | 릴리즈 준비 |

**Examples:**
- `feature/AUTH-123-jwt-authentication`
- `bugfix/API-456-fix-null-pointer`

## Commit Rules

- 간결하고 명확한 영어로 작성
- 현재 시제 사용 ("Add feature" not "Added feature")
- 각 커밋은 독립적으로 의미가 있어야 함
- 관련 없는 변경사항은 별도 커밋으로 분리
- .env, credentials 등 민감한 파일은 커밋하지 않음

## PR Creation (gh CLI)

### PR Title Format

```
<type>(<scope>): <brief description>
```

### PR Body Template

```markdown
## Summary
<!-- 변경 사항을 1-3개 bullet point로 요약 -->

-
-

## Changes
<!-- 주요 변경 파일/로직 설명 -->

-

## Test Plan
<!-- 테스트 방법 체크리스트 -->

- [ ] Unit tests 추가/수정
- [ ] 로컬 테스트 완료
- [ ]

## Related Issues
<!-- 관련 이슈/티켓 링크 -->

Closes #
```

### PR Best Practices

1. **작은 단위로 분리**: 하나의 PR은 하나의 목적
2. **Self-review 먼저**: 제출 전 본인이 먼저 검토
3. **스크린샷 첨부**: UI 변경 시 before/after 이미지
4. **Breaking changes 명시**: API 변경 시 명확히 표시

### gh CLI Usage

```bash
# PR 생성
gh pr create --title "feat(auth): add login" --body "## Summary
- Add login endpoint
- Implement JWT validation

## Test Plan
- [ ] Unit tests 추가
- [ ] 로컬 테스트 완료"

# Draft PR 생성
gh pr create --draft --title "WIP: feature implementation"

# PR 상태 확인
gh pr status
gh pr checks
```
