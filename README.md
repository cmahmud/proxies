# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 298
- HTTP: 380 alive / 66 gold
- HTTPS: 239 alive / 16 gold
- SOCKS4: 201 alive / 116 gold
- SOCKS5: 180 alive / 100 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15613
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
