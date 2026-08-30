# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 419
- HTTP: 124 alive / 79 gold
- HTTPS: 76 alive / 28 gold
- SOCKS4: 158 alive / 150 gold
- SOCKS5: 187 alive / 162 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44046
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
