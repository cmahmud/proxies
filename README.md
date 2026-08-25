# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 418
- HTTP: 102 alive / 65 gold
- HTTPS: 84 alive / 19 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 198 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36045
- Ever gold: 1265

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
