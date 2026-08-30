# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 429
- HTTP: 102 alive / 76 gold
- HTTPS: 59 alive / 25 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44432
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
