# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 409
- HTTP: 92 alive / 57 gold
- HTTPS: 52 alive / 20 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36712
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
