# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 427
- HTTP: 120 alive / 78 gold
- HTTPS: 65 alive / 22 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44324
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
