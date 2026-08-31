# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 441
- HTTP: 122 alive / 76 gold
- HTTPS: 89 alive / 30 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 202 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45456
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
