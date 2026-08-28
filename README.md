# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 386
- HTTP: 90 alive / 67 gold
- HTTPS: 90 alive / 14 gold
- SOCKS4: 157 alive / 152 gold
- SOCKS5: 177 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43230
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
