# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 419
- HTTP: 312 alive / 82 gold
- HTTPS: 206 alive / 25 gold
- SOCKS4: 243 alive / 155 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30211
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
