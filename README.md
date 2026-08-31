# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 439
- HTTP: 112 alive / 75 gold
- HTTPS: 77 alive / 30 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 198 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45556
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
