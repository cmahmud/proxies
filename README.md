# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 420
- HTTP: 106 alive / 65 gold
- HTTPS: 72 alive / 24 gold
- SOCKS4: 188 alive / 161 gold
- SOCKS5: 200 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45524
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
