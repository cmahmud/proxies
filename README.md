# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 433
- HTTP: 132 alive / 89 gold
- HTTPS: 74 alive / 35 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 174 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44077
- Ever gold: 1396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
