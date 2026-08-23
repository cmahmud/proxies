# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 383
- HTTP: 97 alive / 61 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 182 alive / 156 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
