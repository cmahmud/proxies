# SyndProxy private pool

## Current pool

- Alive now: 1178
- Gold now: 420
- HTTP: 431 alive / 96 gold
- HTTPS: 285 alive / 26 gold
- SOCKS4: 221 alive / 139 gold
- SOCKS5: 241 alive / 159 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30417
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
