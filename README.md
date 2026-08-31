# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 429
- HTTP: 118 alive / 72 gold
- HTTPS: 72 alive / 25 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45530
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
