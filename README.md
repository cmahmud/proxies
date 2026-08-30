# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 447
- HTTP: 120 alive / 75 gold
- HTTPS: 138 alive / 41 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44687
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
