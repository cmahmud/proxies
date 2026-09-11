# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 367
- HTTP: 99 alive / 69 gold
- HTTPS: 55 alive / 22 gold
- SOCKS4: 132 alive / 107 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48717
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
