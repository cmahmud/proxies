# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 404
- HTTP: 297 alive / 97 gold
- HTTPS: 222 alive / 23 gold
- SOCKS4: 212 alive / 137 gold
- SOCKS5: 245 alive / 147 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28254
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
