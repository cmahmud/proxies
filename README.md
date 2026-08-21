# SyndProxy private pool

## Current pool

- Alive now: 1181
- Gold now: 423
- HTTP: 419 alive / 102 gold
- HTTPS: 284 alive / 25 gold
- SOCKS4: 225 alive / 139 gold
- SOCKS5: 253 alive / 157 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30426
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
