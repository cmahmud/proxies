# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 432
- HTTP: 115 alive / 85 gold
- HTTPS: 66 alive / 36 gold
- SOCKS4: 157 alive / 152 gold
- SOCKS5: 175 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44088
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
