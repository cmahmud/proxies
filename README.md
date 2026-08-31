# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 433
- HTTP: 99 alive / 74 gold
- HTTPS: 65 alive / 29 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45472
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
