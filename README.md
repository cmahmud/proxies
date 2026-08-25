# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 408
- HTTP: 92 alive / 64 gold
- HTTPS: 70 alive / 18 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36985
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
