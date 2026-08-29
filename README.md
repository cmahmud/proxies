# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 384
- HTTP: 91 alive / 65 gold
- HTTPS: 86 alive / 11 gold
- SOCKS4: 156 alive / 150 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43240
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
