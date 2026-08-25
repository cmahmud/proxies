# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 405
- HTTP: 82 alive / 59 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36446
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
