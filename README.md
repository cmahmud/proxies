# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 415
- HTTP: 94 alive / 64 gold
- HTTPS: 82 alive / 21 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 37016
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
