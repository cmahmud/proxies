# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 383
- HTTP: 94 alive / 44 gold
- HTTPS: 43 alive / 13 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33562
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
