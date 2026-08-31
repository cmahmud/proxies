# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 434
- HTTP: 117 alive / 79 gold
- HTTPS: 98 alive / 26 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 211 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
