# SyndProxy validated proxy pool

## Current pool

- Alive now: 696
- Gold now: 467
- HTTP: 174 alive / 91 gold
- HTTPS: 124 alive / 36 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 232 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45285
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
