# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 399
- HTTP: 89 alive / 68 gold
- HTTPS: 91 alive / 14 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43255
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
