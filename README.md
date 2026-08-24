# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 373
- HTTP: 125 alive / 66 gold
- HTTPS: 63 alive / 14 gold
- SOCKS4: 168 alive / 147 gold
- SOCKS5: 179 alive / 146 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33220
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
