# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 442
- HTTP: 119 alive / 85 gold
- HTTPS: 71 alive / 38 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44105
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
