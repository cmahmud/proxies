# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 417
- HTTP: 89 alive / 67 gold
- HTTPS: 65 alive / 21 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36990
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
