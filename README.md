# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 434
- HTTP: 116 alive / 74 gold
- HTTPS: 70 alive / 29 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45534
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
