# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 432
- HTTP: 109 alive / 70 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45546
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
