# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 402
- HTTP: 80 alive / 61 gold
- HTTPS: 58 alive / 13 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36464
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
