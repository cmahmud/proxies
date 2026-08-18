# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 217
- HTTP: 409 alive / 31 gold
- HTTPS: 185 alive / 10 gold
- SOCKS4: 278 alive / 101 gold
- SOCKS5: 199 alive / 75 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
