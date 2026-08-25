# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 400
- HTTP: 86 alive / 52 gold
- HTTPS: 46 alive / 16 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36601
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
