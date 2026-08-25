# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 398
- HTTP: 84 alive / 57 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36645
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
