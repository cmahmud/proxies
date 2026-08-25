# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 414
- HTTP: 93 alive / 67 gold
- HTTPS: 70 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36979
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
