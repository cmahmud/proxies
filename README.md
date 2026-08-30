# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 429
- HTTP: 100 alive / 75 gold
- HTTPS: 57 alive / 27 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44436
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
