# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 362
- HTTP: 75 alive / 50 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 178 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48289
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
