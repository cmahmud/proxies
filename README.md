# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 454
- HTTP: 132 alive / 86 gold
- HTTPS: 87 alive / 36 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45602
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
