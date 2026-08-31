# SyndProxy validated proxy pool

## Current pool

- Alive now: 673
- Gold now: 482
- HTTP: 168 alive / 101 gold
- HTTPS: 139 alive / 43 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 197 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45238
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
