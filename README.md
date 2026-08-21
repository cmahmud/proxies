# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 404
- HTTP: 276 alive / 91 gold
- HTTPS: 208 alive / 20 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 243 alive / 143 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29256
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
