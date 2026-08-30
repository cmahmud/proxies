# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 419
- HTTP: 119 alive / 76 gold
- HTTPS: 48 alive / 19 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44480
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
