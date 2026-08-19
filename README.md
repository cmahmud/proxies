# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 518
- HTTP: 434 alive / 185 gold
- HTTPS: 311 alive / 53 gold
- SOCKS4: 196 alive / 121 gold
- SOCKS5: 236 alive / 159 gold

## Historical pool

- Discovered: 125606
- Ever alive: 19579
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
