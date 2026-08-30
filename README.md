# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 440
- HTTP: 118 alive / 85 gold
- HTTPS: 68 alive / 37 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44099
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
