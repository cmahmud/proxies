# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 406
- HTTP: 107 alive / 59 gold
- HTTPS: 59 alive / 17 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36786
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
