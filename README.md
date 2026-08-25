# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 419
- HTTP: 101 alive / 66 gold
- HTTPS: 64 alive / 22 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 178 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36971
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
