# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 433
- HTTP: 108 alive / 70 gold
- HTTPS: 60 alive / 27 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45547
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
