# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 418
- HTTP: 112 alive / 73 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44480
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
