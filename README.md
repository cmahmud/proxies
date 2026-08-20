# SyndProxy private pool

## Current pool

- Alive now: 1680
- Gold now: 637
- HTTP: 726 alive / 233 gold
- HTTPS: 537 alive / 136 gold
- SOCKS4: 186 alive / 101 gold
- SOCKS5: 231 alive / 167 gold

## Historical pool

- Discovered: 143425
- Ever alive: 24689
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
