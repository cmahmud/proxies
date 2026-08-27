# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 417
- HTTP: 105 alive / 72 gold
- HTTPS: 99 alive / 25 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 172 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41964
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
