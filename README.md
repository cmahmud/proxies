# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 398
- HTTP: 85 alive / 55 gold
- HTTPS: 58 alive / 17 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36649
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
