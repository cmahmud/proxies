# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 408
- HTTP: 84 alive / 61 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 198 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36698
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
