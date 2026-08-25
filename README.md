# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 399
- HTTP: 94 alive / 55 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36846
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
