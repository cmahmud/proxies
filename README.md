# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 386
- HTTP: 244 alive / 77 gold
- HTTPS: 133 alive / 20 gold
- SOCKS4: 213 alive / 143 gold
- SOCKS5: 204 alive / 146 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25239
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
