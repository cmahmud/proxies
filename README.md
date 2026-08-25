# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 395
- HTTP: 78 alive / 53 gold
- HTTPS: 58 alive / 15 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36616
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
