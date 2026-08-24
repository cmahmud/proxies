# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 391
- HTTP: 120 alive / 65 gold
- HTTPS: 53 alive / 17 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 183 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33258
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
