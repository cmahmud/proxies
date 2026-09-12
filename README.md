# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 452
- HTTP: 126 alive / 95 gold
- HTTPS: 56 alive / 30 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49327
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
