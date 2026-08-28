# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 410
- HTTP: 87 alive / 66 gold
- HTTPS: 88 alive / 15 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43038
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
