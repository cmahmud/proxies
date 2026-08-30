# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 422
- HTTP: 108 alive / 79 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44500
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
