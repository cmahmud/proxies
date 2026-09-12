# SyndProxy validated proxy pool

## Current pool

- Alive now: 392
- Gold now: 327
- HTTP: 80 alive / 63 gold
- HTTPS: 42 alive / 24 gold
- SOCKS4: 121 alive / 109 gold
- SOCKS5: 149 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49500
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
