# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 299
- HTTP: 281 alive / 33 gold
- HTTPS: 200 alive / 6 gold
- SOCKS4: 208 alive / 132 gold
- SOCKS5: 219 alive / 128 gold

## Historical pool

- Discovered: 102843
- Ever alive: 13202
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
