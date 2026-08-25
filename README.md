# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 411
- HTTP: 96 alive / 62 gold
- HTTPS: 75 alive / 21 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 37027
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
