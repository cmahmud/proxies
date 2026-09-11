# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 367
- HTTP: 98 alive / 69 gold
- HTTPS: 59 alive / 22 gold
- SOCKS4: 130 alive / 107 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48717
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
