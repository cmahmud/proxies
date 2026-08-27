# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 422
- HTTP: 102 alive / 75 gold
- HTTPS: 123 alive / 23 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42100
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
