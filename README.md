# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 417
- HTTP: 96 alive / 67 gold
- HTTPS: 70 alive / 23 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36943
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
