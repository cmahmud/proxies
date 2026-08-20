# SyndProxy private pool

## Current pool

- Alive now: 712
- Gold now: 387
- HTTP: 198 alive / 73 gold
- HTTPS: 114 alive / 18 gold
- SOCKS4: 208 alive / 154 gold
- SOCKS5: 192 alive / 142 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25621
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
