# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 408
- HTTP: 90 alive / 59 gold
- HTTPS: 63 alive / 17 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36350
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
