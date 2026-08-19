# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 359
- HTTP: 318 alive / 74 gold
- HTTPS: 221 alive / 10 gold
- SOCKS4: 224 alive / 125 gold
- SOCKS5: 235 alive / 150 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20283
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
