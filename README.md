# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 454
- HTTP: 136 alive / 86 gold
- HTTPS: 92 alive / 36 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 200 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45602
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
