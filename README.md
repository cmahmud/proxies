# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 404
- HTTP: 92 alive / 59 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36442
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
