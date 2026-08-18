# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 352
- HTTP: 334 alive / 52 gold
- HTTPS: 191 alive / 14 gold
- SOCKS4: 256 alive / 147 gold
- SOCKS5: 230 alive / 139 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15102
- Ever gold: 480

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
