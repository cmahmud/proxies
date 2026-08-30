# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 421
- HTTP: 131 alive / 81 gold
- HTTPS: 77 alive / 30 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 234 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43954
- Ever gold: 1381

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
