# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 402
- HTTP: 95 alive / 67 gold
- HTTPS: 38 alive / 20 gold
- SOCKS4: 157 alive / 147 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48806
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
