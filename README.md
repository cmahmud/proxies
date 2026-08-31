# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 440
- HTTP: 139 alive / 78 gold
- HTTPS: 92 alive / 30 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 214 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45407
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
