# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 423
- HTTP: 127 alive / 82 gold
- HTTPS: 77 alive / 29 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44046
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
