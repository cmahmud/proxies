# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 419
- HTTP: 107 alive / 73 gold
- HTTPS: 45 alive / 21 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44479
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
