# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 401
- HTTP: 76 alive / 55 gold
- HTTPS: 46 alive / 14 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 181 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36448
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
