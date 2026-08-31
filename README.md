# SyndProxy validated proxy pool

## Current pool

- Alive now: 713
- Gold now: 468
- HTTP: 172 alive / 92 gold
- HTTPS: 137 alive / 38 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 227 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45300
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
