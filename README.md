# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 367
- HTTP: 317 alive / 60 gold
- HTTPS: 238 alive / 14 gold
- SOCKS4: 253 alive / 151 gold
- SOCKS5: 226 alive / 142 gold

## Historical pool

- Discovered: 109324
- Ever alive: 15175
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
