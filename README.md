# SyndProxy private pool

## Current pool

- Alive now: 1342
- Gold now: 392
- HTTP: 473 alive / 93 gold
- HTTPS: 334 alive / 18 gold
- SOCKS4: 219 alive / 130 gold
- SOCKS5: 316 alive / 151 gold

## Historical pool

- Discovered: 134541
- Ever alive: 22020
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
