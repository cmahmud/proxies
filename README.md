# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 417
- HTTP: 96 alive / 65 gold
- HTTPS: 69 alive / 22 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36964
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
