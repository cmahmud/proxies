# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 473
- HTTP: 302 alive / 119 gold
- HTTPS: 209 alive / 87 gold
- SOCKS4: 179 alive / 130 gold
- SOCKS5: 224 alive / 137 gold

## Historical pool

- Discovered: 117131
- Ever alive: 17532
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
