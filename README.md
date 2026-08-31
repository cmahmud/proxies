# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 435
- HTTP: 115 alive / 76 gold
- HTTPS: 72 alive / 29 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45467
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
