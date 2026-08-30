# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 429
- HTTP: 111 alive / 75 gold
- HTTPS: 55 alive / 27 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44457
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
