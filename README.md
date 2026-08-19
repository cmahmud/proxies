# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 301
- HTTP: 371 alive / 64 gold
- HTTPS: 201 alive / 18 gold
- SOCKS4: 206 alive / 117 gold
- SOCKS5: 186 alive / 102 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15630
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
