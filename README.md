# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 471
- HTTP: 317 alive / 116 gold
- HTTPS: 224 alive / 88 gold
- SOCKS4: 189 alive / 130 gold
- SOCKS5: 227 alive / 137 gold

## Historical pool

- Discovered: 117131
- Ever alive: 17545
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
