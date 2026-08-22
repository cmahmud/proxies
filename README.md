# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 435
- HTTP: 322 alive / 84 gold
- HTTPS: 219 alive / 30 gold
- SOCKS4: 233 alive / 152 gold
- SOCKS5: 257 alive / 169 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32237
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
