# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 403
- HTTP: 93 alive / 59 gold
- HTTPS: 43 alive / 15 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36440
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
