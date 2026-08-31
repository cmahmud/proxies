# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 430
- HTTP: 101 alive / 72 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45472
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
