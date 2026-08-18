# SyndProxy private pool

## Current pool

- Alive now: 815
- Gold now: 217
- HTTP: 274 alive / 31 gold
- HTTPS: 130 alive / 8 gold
- SOCKS4: 226 alive / 102 gold
- SOCKS5: 185 alive / 76 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
