# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 404
- HTTP: 88 alive / 59 gold
- HTTPS: 47 alive / 15 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36446
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
