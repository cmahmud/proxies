# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 408
- HTTP: 107 alive / 63 gold
- HTTPS: 94 alive / 14 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 199 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39299
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
