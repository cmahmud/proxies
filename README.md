# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 455
- HTTP: 134 alive / 87 gold
- HTTPS: 89 alive / 36 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 199 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45602
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
