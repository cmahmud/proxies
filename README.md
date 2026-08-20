# SyndProxy private pool

## Current pool

- Alive now: 1866
- Gold now: 660
- HTTP: 713 alive / 213 gold
- HTTPS: 548 alive / 113 gold
- SOCKS4: 247 alive / 160 gold
- SOCKS5: 358 alive / 174 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24161
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
