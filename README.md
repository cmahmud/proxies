# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 409
- HTTP: 92 alive / 65 gold
- HTTPS: 72 alive / 18 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36983
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
