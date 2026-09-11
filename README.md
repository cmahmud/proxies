# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 369
- HTTP: 96 alive / 70 gold
- HTTPS: 53 alive / 23 gold
- SOCKS4: 131 alive / 107 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48717
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
