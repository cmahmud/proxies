# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 437
- HTTP: 121 alive / 78 gold
- HTTPS: 95 alive / 28 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 206 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1433

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
