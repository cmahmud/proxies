# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 415
- HTTP: 93 alive / 65 gold
- HTTPS: 74 alive / 20 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 37001
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
