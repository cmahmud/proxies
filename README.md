# SyndProxy private pool

## Current pool

- Alive now: 1131
- Gold now: 554
- HTTP: 417 alive / 189 gold
- HTTPS: 287 alive / 104 gold
- SOCKS4: 219 alive / 120 gold
- SOCKS5: 208 alive / 141 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19298
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
