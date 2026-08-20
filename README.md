# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 367
- HTTP: 164 alive / 71 gold
- HTTPS: 151 alive / 20 gold
- SOCKS4: 180 alive / 119 gold
- SOCKS5: 225 alive / 157 gold

## Historical pool

- Discovered: 148330
- Ever alive: 26050
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
