# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 412
- HTTP: 108 alive / 62 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45519
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
