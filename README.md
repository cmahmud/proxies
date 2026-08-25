# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 411
- HTTP: 95 alive / 59 gold
- HTTPS: 49 alive / 20 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36708
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
