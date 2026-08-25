# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 411
- HTTP: 87 alive / 65 gold
- HTTPS: 46 alive / 19 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36749
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
