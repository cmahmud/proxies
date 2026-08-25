# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 410
- HTTP: 93 alive / 60 gold
- HTTPS: 83 alive / 21 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36919
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
