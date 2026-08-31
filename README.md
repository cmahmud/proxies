# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 421
- HTTP: 86 alive / 59 gold
- HTTPS: 66 alive / 27 gold
- SOCKS4: 181 alive / 165 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45500
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
