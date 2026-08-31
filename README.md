# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 406
- HTTP: 98 alive / 54 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45508
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
