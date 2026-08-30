# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 428
- HTTP: 117 alive / 72 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44406
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
