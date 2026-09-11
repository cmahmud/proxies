# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 409
- HTTP: 90 alive / 64 gold
- HTTPS: 40 alive / 20 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48843
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
