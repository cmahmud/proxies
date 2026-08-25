# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 414
- HTTP: 89 alive / 65 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36999
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
