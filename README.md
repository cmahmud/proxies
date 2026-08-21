# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 401
- HTTP: 257 alive / 76 gold
- HTTPS: 193 alive / 19 gold
- SOCKS4: 214 alive / 145 gold
- SOCKS5: 249 alive / 161 gold

## Historical pool

- Discovered: 155790
- Ever alive: 29326
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
