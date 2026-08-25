# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 396
- HTTP: 97 alive / 55 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36823
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
