# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 441
- HTTP: 139 alive / 76 gold
- HTTPS: 105 alive / 32 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 207 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45392
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
