# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 401
- HTTP: 295 alive / 91 gold
- HTTPS: 158 alive / 25 gold
- SOCKS4: 231 alive / 146 gold
- SOCKS5: 227 alive / 139 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29377
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
