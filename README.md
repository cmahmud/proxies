# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 391
- HTTP: 98 alive / 60 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 187 alive / 156 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33339
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
