# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 413
- HTTP: 79 alive / 63 gold
- HTTPS: 38 alive / 22 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 180 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48827
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
