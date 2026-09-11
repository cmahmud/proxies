# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 357
- HTTP: 102 alive / 70 gold
- HTTPS: 52 alive / 23 gold
- SOCKS4: 109 alive / 96 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48708
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
