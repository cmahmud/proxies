# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 402
- HTTP: 102 alive / 56 gold
- HTTPS: 68 alive / 19 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36812
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
