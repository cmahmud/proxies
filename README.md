# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 432
- HTTP: 133 alive / 89 gold
- HTTPS: 74 alive / 34 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 173 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44077
- Ever gold: 1396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
