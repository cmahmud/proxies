# SyndProxy private pool

## Current pool

- Alive now: 708
- Gold now: 387
- HTTP: 172 alive / 65 gold
- HTTPS: 114 alive / 19 gold
- SOCKS4: 210 alive / 147 gold
- SOCKS5: 212 alive / 156 gold

## Historical pool

- Discovered: 146656
- Ever alive: 25692
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
