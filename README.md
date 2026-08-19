# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 343
- HTTP: 287 alive / 70 gold
- HTTPS: 214 alive / 16 gold
- SOCKS4: 196 alive / 111 gold
- SOCKS5: 231 alive / 146 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16129
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
