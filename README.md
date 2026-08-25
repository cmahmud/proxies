# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 408
- HTTP: 94 alive / 60 gold
- HTTPS: 78 alive / 20 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36915
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
