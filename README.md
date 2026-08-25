# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 400
- HTTP: 85 alive / 57 gold
- HTTPS: 55 alive / 15 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36477
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
