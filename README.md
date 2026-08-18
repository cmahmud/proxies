# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 218
- HTTP: 314 alive / 27 gold
- HTTPS: 140 alive / 10 gold
- SOCKS4: 221 alive / 98 gold
- SOCKS5: 237 alive / 83 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7957
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
