# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 416
- HTTP: 110 alive / 76 gold
- HTTPS: 63 alive / 29 gold
- SOCKS4: 156 alive / 153 gold
- SOCKS5: 167 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
