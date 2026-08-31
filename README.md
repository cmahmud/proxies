# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 435
- HTTP: 115 alive / 75 gold
- HTTPS: 71 alive / 29 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45534
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
