# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 400
- HTTP: 79 alive / 59 gold
- HTTPS: 60 alive / 13 gold
- SOCKS4: 190 alive / 160 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36399
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
