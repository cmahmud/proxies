# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 343
- HTTP: 331 alive / 68 gold
- HTTPS: 267 alive / 18 gold
- SOCKS4: 235 alive / 141 gold
- SOCKS5: 212 alive / 116 gold

## Historical pool

- Discovered: 110913
- Ever alive: 16091
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
