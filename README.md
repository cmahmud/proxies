# SyndProxy private pool

## Current pool

- Alive now: 1146
- Gold now: 251
- HTTP: 381 alive / 28 gold
- HTTPS: 286 alive / 10 gold
- SOCKS4: 237 alive / 111 gold
- SOCKS5: 242 alive / 102 gold

## Historical pool

- Discovered: 94370
- Ever alive: 10174
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
