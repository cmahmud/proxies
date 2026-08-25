# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 408
- HTTP: 97 alive / 60 gold
- HTTPS: 77 alive / 22 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36923
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
