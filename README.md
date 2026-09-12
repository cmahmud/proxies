# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 422
- HTTP: 101 alive / 75 gold
- HTTPS: 45 alive / 25 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49477
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
