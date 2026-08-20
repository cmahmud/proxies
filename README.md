# SyndProxy private pool

## Current pool

- Alive now: 1554
- Gold now: 633
- HTTP: 525 alive / 212 gold
- HTTPS: 435 alive / 114 gold
- SOCKS4: 234 alive / 148 gold
- SOCKS5: 360 alive / 159 gold

## Historical pool

- Discovered: 141233
- Ever alive: 24111
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
