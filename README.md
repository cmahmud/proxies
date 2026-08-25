# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 406
- HTTP: 100 alive / 60 gold
- HTTPS: 55 alive / 16 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36783
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
