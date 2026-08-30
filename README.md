# SyndProxy validated proxy pool

## Current pool

- Alive now: 671
- Gold now: 419
- HTTP: 138 alive / 80 gold
- HTTPS: 88 alive / 29 gold
- SOCKS4: 164 alive / 150 gold
- SOCKS5: 281 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43861
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
