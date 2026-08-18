# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 350
- HTTP: 316 alive / 51 gold
- HTTPS: 189 alive / 14 gold
- SOCKS4: 254 alive / 146 gold
- SOCKS5: 227 alive / 139 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15102
- Ever gold: 480

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
