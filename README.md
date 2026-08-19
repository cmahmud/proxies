# SyndProxy private pool

## Current pool

- Alive now: 1166
- Gold now: 412
- HTTP: 382 alive / 82 gold
- HTTPS: 256 alive / 15 gold
- SOCKS4: 264 alive / 155 gold
- SOCKS5: 264 alive / 160 gold

## Historical pool

- Discovered: 131729
- Ever alive: 20790
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
