# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 416
- HTTP: 92 alive / 65 gold
- HTTPS: 72 alive / 21 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36961
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
