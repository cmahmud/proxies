# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 401
- HTTP: 257 alive / 91 gold
- HTTPS: 194 alive / 29 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 239 alive / 134 gold

## Historical pool

- Discovered: 161987
- Ever alive: 31297
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
