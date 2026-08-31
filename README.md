# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 430
- HTTP: 100 alive / 73 gold
- HTTPS: 69 alive / 27 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45472
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
