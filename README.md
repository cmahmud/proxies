# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 442
- HTTP: 115 alive / 77 gold
- HTTPS: 88 alive / 30 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 200 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45452
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
