# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 418
- HTTP: 92 alive / 66 gold
- HTTPS: 73 alive / 21 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36996
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
