# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 411
- HTTP: 89 alive / 57 gold
- HTTPS: 70 alive / 26 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45510
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
