# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 419
- HTTP: 96 alive / 66 gold
- HTTPS: 72 alive / 24 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36954
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
