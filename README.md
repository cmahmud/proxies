# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 436
- HTTP: 117 alive / 80 gold
- HTTPS: 92 alive / 27 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 208 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
