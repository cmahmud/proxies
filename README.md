# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 423
- HTTP: 96 alive / 68 gold
- HTTPS: 64 alive / 25 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36950
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
