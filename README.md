# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 409
- HTTP: 96 alive / 61 gold
- HTTPS: 68 alive / 21 gold
- SOCKS4: 186 alive / 161 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36930
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
