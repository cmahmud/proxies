# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 432
- HTTP: 107 alive / 72 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45547
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
