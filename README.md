# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 417
- HTTP: 122 alive / 78 gold
- HTTPS: 77 alive / 28 gold
- SOCKS4: 158 alive / 150 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44046
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
