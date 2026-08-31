# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 433
- HTTP: 103 alive / 74 gold
- HTTPS: 67 alive / 27 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45470
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
