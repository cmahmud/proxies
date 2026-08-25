# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 414
- HTTP: 96 alive / 60 gold
- HTTPS: 69 alive / 19 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36221
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
