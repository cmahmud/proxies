# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 398
- HTTP: 97 alive / 53 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36601
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
