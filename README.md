# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 349
- HTTP: 305 alive / 50 gold
- HTTPS: 199 alive / 15 gold
- SOCKS4: 237 alive / 142 gold
- SOCKS5: 236 alive / 142 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14685
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
