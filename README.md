# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 409
- HTTP: 95 alive / 60 gold
- HTTPS: 67 alive / 22 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36928
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
