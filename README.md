# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 407
- HTTP: 83 alive / 59 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36353
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
