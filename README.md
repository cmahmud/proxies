# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 410
- HTTP: 88 alive / 59 gold
- HTTPS: 48 alive / 19 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36717
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
