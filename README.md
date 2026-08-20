# SyndProxy private pool

## Current pool

- Alive now: 1551
- Gold now: 632
- HTTP: 517 alive / 212 gold
- HTTPS: 443 alive / 113 gold
- SOCKS4: 233 alive / 148 gold
- SOCKS5: 358 alive / 159 gold

## Historical pool

- Discovered: 141232
- Ever alive: 24107
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
