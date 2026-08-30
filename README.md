# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 438
- HTTP: 125 alive / 92 gold
- HTTPS: 72 alive / 31 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 174 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44094
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
