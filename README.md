# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 483
- HTTP: 160 alive / 104 gold
- HTTPS: 140 alive / 40 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 199 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45240
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
