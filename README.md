# SyndProxy private pool

## Current pool

- Alive now: 1204
- Gold now: 423
- HTTP: 438 alive / 101 gold
- HTTPS: 275 alive / 25 gold
- SOCKS4: 234 alive / 139 gold
- SOCKS5: 257 alive / 158 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30430
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
