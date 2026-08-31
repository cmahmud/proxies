# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 449
- HTTP: 126 alive / 85 gold
- HTTPS: 73 alive / 30 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45563
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
