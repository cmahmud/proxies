# SyndProxy private pool

## Current pool

- Alive now: 885
- Gold now: 401
- HTTP: 259 alive / 83 gold
- HTTPS: 194 alive / 24 gold
- SOCKS4: 217 alive / 149 gold
- SOCKS5: 215 alive / 145 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27479
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
