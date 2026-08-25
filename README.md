# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 400
- HTTP: 86 alive / 61 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36467
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
