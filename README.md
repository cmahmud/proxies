# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 410
- HTTP: 82 alive / 62 gold
- HTTPS: 37 alive / 21 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48829
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
