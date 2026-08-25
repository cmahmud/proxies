# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 402
- HTTP: 79 alive / 59 gold
- HTTPS: 53 alive / 14 gold
- SOCKS4: 191 alive / 160 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36394
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
