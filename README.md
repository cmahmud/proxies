# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 401
- HTTP: 83 alive / 57 gold
- HTTPS: 51 alive / 14 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36477
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
