# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 406
- HTTP: 79 alive / 59 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36701
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
