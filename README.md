# SyndProxy validated proxy pool

## Current pool

- Alive now: 436
- Gold now: 357
- HTTP: 82 alive / 71 gold
- HTTPS: 48 alive / 32 gold
- SOCKS4: 111 alive / 76 gold
- SOCKS5: 195 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48586
- Ever gold: 1557

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
