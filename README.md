# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 417
- HTTP: 111 alive / 74 gold
- HTTPS: 45 alive / 18 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44481
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
