# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 418
- HTTP: 95 alive / 64 gold
- HTTPS: 54 alive / 25 gold
- SOCKS4: 196 alive / 168 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49070
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
