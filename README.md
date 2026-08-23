# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 304
- HTTP: 126 alive / 36 gold
- HTTPS: 65 alive / 10 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 182 alive / 106 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32825
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
