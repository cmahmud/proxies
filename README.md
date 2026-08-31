# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 419
- HTTP: 107 alive / 65 gold
- HTTPS: 72 alive / 23 gold
- SOCKS4: 187 alive / 161 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45524
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
