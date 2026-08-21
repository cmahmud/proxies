# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 401
- HTTP: 322 alive / 81 gold
- HTTPS: 212 alive / 21 gold
- SOCKS4: 223 alive / 147 gold
- SOCKS5: 272 alive / 152 gold

## Historical pool

- Discovered: 156433
- Ever alive: 29542
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
