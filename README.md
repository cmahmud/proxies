# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 409
- HTTP: 97 alive / 61 gold
- HTTPS: 68 alive / 21 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36927
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
