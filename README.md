# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 401
- HTTP: 333 alive / 85 gold
- HTTPS: 220 alive / 25 gold
- SOCKS4: 217 alive / 134 gold
- SOCKS5: 248 alive / 157 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32418
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
