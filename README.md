# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 445
- HTTP: 119 alive / 81 gold
- HTTPS: 110 alive / 31 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45639
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
