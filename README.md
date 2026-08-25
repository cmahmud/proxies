# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 400
- HTTP: 84 alive / 61 gold
- HTTPS: 49 alive / 14 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36466
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
