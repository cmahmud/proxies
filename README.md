# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 423
- HTTP: 128 alive / 83 gold
- HTTPS: 80 alive / 29 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44046
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
