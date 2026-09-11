# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 427
- HTTP: 91 alive / 72 gold
- HTTPS: 52 alive / 25 gold
- SOCKS4: 201 alive / 169 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49085
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
