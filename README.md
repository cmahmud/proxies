# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 416
- HTTP: 96 alive / 67 gold
- HTTPS: 69 alive / 22 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 171 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37055
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
