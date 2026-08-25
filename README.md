# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 400
- HTTP: 77 alive / 57 gold
- HTTPS: 59 alive / 14 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36483
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
