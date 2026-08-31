# SyndProxy validated proxy pool

## Current pool

- Alive now: 710
- Gold now: 468
- HTTP: 179 alive / 93 gold
- HTTPS: 127 alive / 36 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 232 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45285
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
