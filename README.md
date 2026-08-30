# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 422
- HTTP: 114 alive / 76 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44490
- Ever gold: 1402

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
