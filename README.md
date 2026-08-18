# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 283
- HTTP: 304 alive / 28 gold
- HTTPS: 158 alive / 5 gold
- SOCKS4: 228 alive / 136 gold
- SOCKS5: 220 alive / 114 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12502
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
