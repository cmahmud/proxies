# SyndProxy validated proxy pool

## Current pool

- Alive now: 696
- Gold now: 452
- HTTP: 156 alive / 87 gold
- HTTPS: 130 alive / 30 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 236 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45316
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
