# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 417
- HTTP: 88 alive / 68 gold
- HTTPS: 61 alive / 21 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36987
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
