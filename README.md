# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 403
- HTTP: 96 alive / 60 gold
- HTTPS: 73 alive / 15 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36389
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
