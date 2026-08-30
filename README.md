# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 445
- HTTP: 126 alive / 85 gold
- HTTPS: 69 alive / 29 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43695
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
