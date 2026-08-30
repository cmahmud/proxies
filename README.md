# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 430
- HTTP: 107 alive / 75 gold
- HTTPS: 45 alive / 25 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44446
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
