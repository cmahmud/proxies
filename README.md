# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 421
- HTTP: 89 alive / 60 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 181 alive / 165 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45501
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
