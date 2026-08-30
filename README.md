# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 451
- HTTP: 120 alive / 83 gold
- HTTPS: 141 alive / 39 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44740
- Ever gold: 1412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
