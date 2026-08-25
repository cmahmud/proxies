# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 401
- HTTP: 73 alive / 58 gold
- HTTPS: 37 alive / 13 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36515
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
