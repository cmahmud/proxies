# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 402
- HTTP: 99 alive / 55 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36845
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
