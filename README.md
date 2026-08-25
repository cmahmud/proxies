# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 417
- HTTP: 95 alive / 63 gold
- HTTPS: 76 alive / 19 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36121
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
