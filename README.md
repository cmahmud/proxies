# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 399
- HTTP: 76 alive / 56 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36485
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
