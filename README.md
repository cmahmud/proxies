# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 408
- HTTP: 81 alive / 60 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36361
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
