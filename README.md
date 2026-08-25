# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 418
- HTTP: 95 alive / 64 gold
- HTTPS: 64 alive / 23 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36968
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
