# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 383
- HTTP: 241 alive / 77 gold
- HTTPS: 140 alive / 19 gold
- SOCKS4: 208 alive / 143 gold
- SOCKS5: 205 alive / 144 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25236
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
