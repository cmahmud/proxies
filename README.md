# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 389
- HTTP: 123 alive / 57 gold
- HTTPS: 62 alive / 12 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
