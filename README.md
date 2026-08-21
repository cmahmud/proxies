# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 403
- HTTP: 320 alive / 99 gold
- HTTPS: 236 alive / 25 gold
- SOCKS4: 215 alive / 134 gold
- SOCKS5: 241 alive / 145 gold

## Historical pool

- Discovered: 152750
- Ever alive: 28243
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
