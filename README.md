# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 412
- HTTP: 108 alive / 63 gold
- HTTPS: 69 alive / 20 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45519
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
