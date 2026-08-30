# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 429
- HTTP: 131 alive / 85 gold
- HTTPS: 75 alive / 32 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44085
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
