# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 404
- HTTP: 273 alive / 79 gold
- HTTPS: 211 alive / 12 gold
- SOCKS4: 261 alive / 153 gold
- SOCKS5: 252 alive / 160 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20562
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
