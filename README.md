# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 356
- HTTP: 264 alive / 51 gold
- HTTPS: 214 alive / 16 gold
- SOCKS4: 229 alive / 148 gold
- SOCKS5: 244 alive / 141 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14752
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
