# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 399
- HTTP: 90 alive / 57 gold
- HTTPS: 56 alive / 17 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36839
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
