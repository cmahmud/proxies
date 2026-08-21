# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 405
- HTTP: 359 alive / 110 gold
- HTTPS: 272 alive / 29 gold
- SOCKS4: 201 alive / 144 gold
- SOCKS5: 224 alive / 122 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28492
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
