# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 429
- HTTP: 110 alive / 79 gold
- HTTPS: 115 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42431
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
