# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 369
- HTTP: 78 alive / 44 gold
- HTTPS: 33 alive / 11 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 177 alive / 159 gold

## Historical pool

- Discovered: 173048
- Ever alive: 32987
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
