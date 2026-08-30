# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 430
- HTTP: 124 alive / 88 gold
- HTTPS: 80 alive / 31 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 177 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44083
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
