# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 440
- HTTP: 103 alive / 81 gold
- HTTPS: 70 alive / 29 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 197 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44567
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
