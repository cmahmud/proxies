# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 410
- HTTP: 90 alive / 63 gold
- HTTPS: 65 alive / 17 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36372
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
