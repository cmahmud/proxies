# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 379
- HTTP: 94 alive / 60 gold
- HTTPS: 41 alive / 8 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 195 alive / 155 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
