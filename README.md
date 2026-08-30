# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 414
- HTTP: 120 alive / 78 gold
- HTTPS: 54 alive / 28 gold
- SOCKS4: 165 alive / 150 gold
- SOCKS5: 169 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43701
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
