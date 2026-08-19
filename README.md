# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 465
- HTTP: 283 alive / 119 gold
- HTTPS: 207 alive / 86 gold
- SOCKS4: 186 alive / 124 gold
- SOCKS5: 218 alive / 136 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17495
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
