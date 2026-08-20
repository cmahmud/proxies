# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 386
- HTTP: 187 alive / 63 gold
- HTTPS: 100 alive / 18 gold
- SOCKS4: 199 alive / 149 gold
- SOCKS5: 215 alive / 156 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25694
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
