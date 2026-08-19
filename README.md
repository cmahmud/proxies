# SyndProxy private pool

## Current pool

- Alive now: 1180
- Gold now: 540
- HTTP: 431 alive / 164 gold
- HTTPS: 301 alive / 90 gold
- SOCKS4: 218 alive / 140 gold
- SOCKS5: 230 alive / 146 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18637
- Ever gold: 722

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
