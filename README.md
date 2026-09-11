# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 413
- HTTP: 86 alive / 62 gold
- HTTPS: 38 alive / 22 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48824
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
