# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 397
- HTTP: 402 alive / 93 gold
- HTTPS: 258 alive / 22 gold
- SOCKS4: 185 alive / 112 gold
- SOCKS5: 258 alive / 170 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32447
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
