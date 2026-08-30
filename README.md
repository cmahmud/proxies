# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 425
- HTTP: 112 alive / 72 gold
- HTTPS: 61 alive / 25 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 197 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44452
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
