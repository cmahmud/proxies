# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 400
- HTTP: 84 alive / 55 gold
- HTTPS: 57 alive / 17 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36654
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
