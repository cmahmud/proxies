# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 540
- HTTP: 368 alive / 160 gold
- HTTPS: 239 alive / 95 gold
- SOCKS4: 243 alive / 148 gold
- SOCKS5: 202 alive / 137 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18891
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
