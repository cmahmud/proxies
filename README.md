# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 403
- HTTP: 105 alive / 58 gold
- HTTPS: 54 alive / 18 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36792
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
