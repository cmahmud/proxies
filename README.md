# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 329
- HTTP: 287 alive / 57 gold
- HTTPS: 196 alive / 8 gold
- SOCKS4: 238 alive / 142 gold
- SOCKS5: 220 alive / 122 gold

## Historical pool

- Discovered: 129271
- Ever alive: 20256
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
