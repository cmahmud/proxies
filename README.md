# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 411
- HTTP: 95 alive / 60 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36720
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
