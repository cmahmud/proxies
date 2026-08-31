# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 442
- HTTP: 122 alive / 80 gold
- HTTPS: 74 alive / 28 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 198 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45561
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
