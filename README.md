# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 467
- HTTP: 176 alive / 92 gold
- HTTPS: 119 alive / 36 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 231 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45286
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
