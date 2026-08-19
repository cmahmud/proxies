# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 541
- HTTP: 391 alive / 163 gold
- HTTPS: 274 alive / 92 gold
- SOCKS4: 211 alive / 133 gold
- SOCKS5: 224 alive / 153 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18753
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
