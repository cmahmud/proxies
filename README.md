# SyndProxy private pool

## Current pool

- Alive now: 1215
- Gold now: 531
- HTTP: 448 alive / 182 gold
- HTTPS: 331 alive / 81 gold
- SOCKS4: 223 alive / 128 gold
- SOCKS5: 213 alive / 140 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19778
- Ever gold: 797

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
