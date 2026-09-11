# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 403
- HTTP: 96 alive / 67 gold
- HTTPS: 37 alive / 20 gold
- SOCKS4: 153 alive / 148 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48808
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
