# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 422
- HTTP: 102 alive / 73 gold
- HTTPS: 46 alive / 24 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49479
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
