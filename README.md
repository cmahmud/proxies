# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 406
- HTTP: 102 alive / 61 gold
- HTTPS: 55 alive / 15 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36783
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
