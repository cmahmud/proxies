# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 441
- HTTP: 121 alive / 80 gold
- HTTPS: 84 alive / 28 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 201 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
