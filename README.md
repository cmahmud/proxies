# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 391
- HTTP: 100 alive / 60 gold
- HTTPS: 47 alive / 11 gold
- SOCKS4: 185 alive / 157 gold
- SOCKS5: 193 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33339
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
