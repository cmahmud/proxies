# SyndProxy validated proxy pool

## Current pool

- Alive now: 443
- Gold now: 356
- HTTP: 121 alive / 79 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 81 alive / 75 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48656
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
