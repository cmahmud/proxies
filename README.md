# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 421
- HTTP: 88 alive / 59 gold
- HTTPS: 69 alive / 27 gold
- SOCKS4: 181 alive / 165 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45501
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
