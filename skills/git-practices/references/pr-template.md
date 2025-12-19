# PR Template Guide

## PR Title Format

```
<type>(<scope>): <brief description>
```

**Examples:**
- `feat(auth): implement OAuth2 login flow`
- `fix(api): resolve race condition in order processing`

## PR Body Template

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

## PR Best Practices

1. **작은 단위로 분리**: 하나의 PR은 하나의 목적
2. **Self-review 먼저**: 제출 전 본인이 먼저 검토
3. **스크린샷 첨부**: UI 변경 시 before/after 이미지
4. **Breaking changes 명시**: API 변경 시 명확히 표시

## gh CLI Usage

```bash
# PR 생성
gh pr create --title "feat(auth): add login" --body "## Summary
- Add login endpoint
- Implement JWT validation"

# Draft PR 생성
gh pr create --draft --title "WIP: feature implementation"

# PR 상태 확인
gh pr status
gh pr checks
```
