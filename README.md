# SyndProxy private pool

## Current pool

- Alive now: 1220
- Gold now: 522
- HTTP: 437 alive / 182 gold
- HTTPS: 341 alive / 59 gold
- SOCKS4: 204 alive / 121 gold
- SOCKS5: 238 alive / 160 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19628
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
