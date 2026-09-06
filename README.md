# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 379
- HTTP: 103 alive / 62 gold
- HTTPS: 39 alive / 13 gold
- SOCKS4: 178 alive / 151 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48114
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
