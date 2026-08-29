# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 386
- HTTP: 89 alive / 62 gold
- HTTPS: 48 alive / 20 gold
- SOCKS4: 160 alive / 152 gold
- SOCKS5: 166 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43647
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
