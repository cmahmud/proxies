# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 403
- HTTP: 83 alive / 56 gold
- HTTPS: 47 alive / 18 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36647
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
