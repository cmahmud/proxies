# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 423
- HTTP: 106 alive / 78 gold
- HTTPS: 52 alive / 19 gold
- SOCKS4: 161 alive / 161 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44504
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
