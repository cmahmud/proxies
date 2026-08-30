# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 439
- HTTP: 118 alive / 85 gold
- HTTPS: 67 alive / 37 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 186 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44097
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
