# SyndProxy private pool

## Current pool

- Alive now: 1196
- Gold now: 562
- HTTP: 449 alive / 185 gold
- HTTPS: 277 alive / 111 gold
- SOCKS4: 241 alive / 122 gold
- SOCKS5: 229 alive / 144 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19284
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
