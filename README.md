# SyndProxy validated proxy pool

## Current pool

- Alive now: 697
- Gold now: 468
- HTTP: 165 alive / 93 gold
- HTTPS: 127 alive / 37 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 237 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45279
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
