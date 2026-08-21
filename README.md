# SyndProxy private pool

## Current pool

- Alive now: 854
- Gold now: 364
- HTTP: 293 alive / 73 gold
- HTTPS: 178 alive / 20 gold
- SOCKS4: 182 alive / 128 gold
- SOCKS5: 201 alive / 143 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29669
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
