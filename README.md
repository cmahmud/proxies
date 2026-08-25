# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 401
- HTTP: 85 alive / 61 gold
- HTTPS: 49 alive / 14 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36466
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
