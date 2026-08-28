# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 403
- HTTP: 95 alive / 62 gold
- HTTPS: 89 alive / 18 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42694
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
