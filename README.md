# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 424
- HTTP: 94 alive / 64 gold
- HTTPS: 71 alive / 29 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45491
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
