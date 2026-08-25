# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 401
- HTTP: 84 alive / 58 gold
- HTTPS: 58 alive / 15 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36477
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
