# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 373
- HTTP: 291 alive / 72 gold
- HTTPS: 184 alive / 21 gold
- SOCKS4: 198 alive / 137 gold
- SOCKS5: 207 alive / 143 gold

## Historical pool

- Discovered: 157407
- Ever alive: 29677
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
