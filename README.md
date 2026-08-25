# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 409
- HTTP: 89 alive / 60 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36325
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
