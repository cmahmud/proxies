# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 464
- HTTP: 132 alive / 98 gold
- HTTPS: 61 alive / 33 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49339
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
