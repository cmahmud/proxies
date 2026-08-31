# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 431
- HTTP: 108 alive / 72 gold
- HTTPS: 64 alive / 25 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45547
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
