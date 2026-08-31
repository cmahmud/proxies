# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 427
- HTTP: 95 alive / 70 gold
- HTTPS: 61 alive / 27 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45480
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
