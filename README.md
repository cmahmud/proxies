# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 442
- HTTP: 117 alive / 77 gold
- HTTPS: 83 alive / 30 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 203 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45456
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
