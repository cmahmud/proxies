# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 427
- HTTP: 114 alive / 71 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45530
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
