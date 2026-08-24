# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 388
- HTTP: 88 alive / 55 gold
- HTTPS: 36 alive / 13 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33481
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
