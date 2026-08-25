# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 399
- HTTP: 87 alive / 57 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36839
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
