# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 399
- HTTP: 96 alive / 56 gold
- HTTPS: 57 alive / 19 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36836
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
