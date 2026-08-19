# SyndProxy private pool

## Current pool

- Alive now: 1162
- Gold now: 547
- HTTP: 434 alive / 167 gold
- HTTPS: 286 alive / 92 gold
- SOCKS4: 217 alive / 134 gold
- SOCKS5: 225 alive / 154 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18750
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
