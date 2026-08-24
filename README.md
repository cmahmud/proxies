# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 390
- HTTP: 92 alive / 53 gold
- HTTPS: 54 alive / 12 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33554
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
