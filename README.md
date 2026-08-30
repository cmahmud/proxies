# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 467
- HTTP: 134 alive / 95 gold
- HTTPS: 129 alive / 39 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44840
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
