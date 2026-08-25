# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 405
- HTTP: 97 alive / 59 gold
- HTTPS: 68 alive / 18 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36864
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
