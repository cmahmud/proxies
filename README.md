# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 446
- HTTP: 145 alive / 91 gold
- HTTPS: 79 alive / 32 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 197 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44285
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
