# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 436
- HTTP: 110 alive / 74 gold
- HTTPS: 60 alive / 29 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 200 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45553
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
