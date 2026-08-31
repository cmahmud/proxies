# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 448
- HTTP: 121 alive / 85 gold
- HTTPS: 74 alive / 29 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45563
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
