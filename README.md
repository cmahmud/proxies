# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 417
- HTTP: 99 alive / 72 gold
- HTTPS: 115 alive / 22 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41984
- Ever gold: 1347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
