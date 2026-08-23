# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 207
- HTTP: 110 alive / 45 gold
- HTTPS: 73 alive / 8 gold
- SOCKS4: 75 alive / 68 gold
- SOCKS5: 121 alive / 86 gold

## Historical pool

- Discovered: 169854
- Ever alive: 32707
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
