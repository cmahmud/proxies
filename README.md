# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 436
- HTTP: 120 alive / 88 gold
- HTTPS: 67 alive / 36 gold
- SOCKS4: 155 alive / 152 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44088
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
