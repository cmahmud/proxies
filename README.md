# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 446
- HTTP: 122 alive / 81 gold
- HTTPS: 133 alive / 38 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44738
- Ever gold: 1412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
