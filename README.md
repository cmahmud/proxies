# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 409
- HTTP: 403 alive / 104 gold
- HTTPS: 278 alive / 28 gold
- SOCKS4: 210 alive / 135 gold
- SOCKS5: 241 alive / 142 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28271
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
