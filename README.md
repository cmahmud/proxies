# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 418
- HTTP: 116 alive / 73 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44481
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
