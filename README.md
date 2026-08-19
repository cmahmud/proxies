# SyndProxy private pool

## Current pool

- Alive now: 1218
- Gold now: 381
- HTTP: 402 alive / 90 gold
- HTTPS: 290 alive / 22 gold
- SOCKS4: 230 alive / 125 gold
- SOCKS5: 296 alive / 144 gold

## Historical pool

- Discovered: 134556
- Ever alive: 22139
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
