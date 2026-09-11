# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 422
- HTTP: 89 alive / 69 gold
- HTTPS: 58 alive / 23 gold
- SOCKS4: 188 alive / 166 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49063
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
