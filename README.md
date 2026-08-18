# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 336
- HTTP: 273 alive / 48 gold
- HTTPS: 204 alive / 10 gold
- SOCKS4: 213 alive / 140 gold
- SOCKS5: 229 alive / 138 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14536
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
