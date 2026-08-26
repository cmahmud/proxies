# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 388
- HTTP: 115 alive / 64 gold
- HTTPS: 94 alive / 21 gold
- SOCKS4: 169 alive / 148 gold
- SOCKS5: 184 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39340
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
