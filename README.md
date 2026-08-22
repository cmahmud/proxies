# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 401
- HTTP: 276 alive / 90 gold
- HTTPS: 212 alive / 24 gold
- SOCKS4: 214 alive / 133 gold
- SOCKS5: 252 alive / 154 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31334
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
