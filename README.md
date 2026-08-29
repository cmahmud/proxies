# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 391
- HTTP: 84 alive / 68 gold
- HTTPS: 91 alive / 13 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 177 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43247
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
