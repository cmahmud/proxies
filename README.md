# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 421
- HTTP: 89 alive / 67 gold
- HTTPS: 81 alive / 23 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 37014
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
