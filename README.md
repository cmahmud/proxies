# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 399
- HTTP: 98 alive / 56 gold
- HTTPS: 51 alive / 19 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36832
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
