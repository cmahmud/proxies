# SyndProxy private pool

## Current pool

- Alive now: 1354
- Gold now: 376
- HTTP: 454 alive / 88 gold
- HTTPS: 319 alive / 20 gold
- SOCKS4: 252 alive / 127 gold
- SOCKS5: 329 alive / 141 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22038
- Ever gold: 891

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
