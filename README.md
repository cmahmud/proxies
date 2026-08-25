# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 410
- HTTP: 98 alive / 63 gold
- HTTPS: 63 alive / 20 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36936
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
