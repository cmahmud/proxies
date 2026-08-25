# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 415
- HTTP: 80 alive / 58 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36299
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
