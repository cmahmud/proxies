# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 431
- HTTP: 117 alive / 71 gold
- HTTPS: 68 alive / 26 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45547
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
