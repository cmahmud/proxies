# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 455
- HTTP: 118 alive / 87 gold
- HTTPS: 96 alive / 36 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 203 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45605
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
