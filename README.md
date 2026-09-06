# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 404
- HTTP: 114 alive / 77 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 176 alive / 150 gold
- SOCKS5: 185 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48072
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
