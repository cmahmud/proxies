# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 342
- HTTP: 257 alive / 47 gold
- HTTPS: 238 alive / 10 gold
- SOCKS4: 208 alive / 139 gold
- SOCKS5: 242 alive / 146 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14522
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
