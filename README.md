# SyndProxy private pool

## Current pool

- Alive now: 1250
- Gold now: 404
- HTTP: 415 alive / 86 gold
- HTTPS: 273 alive / 17 gold
- SOCKS4: 244 alive / 148 gold
- SOCKS5: 318 alive / 153 gold

## Historical pool

- Discovered: 134540
- Ever alive: 21977
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
