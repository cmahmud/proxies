# SyndProxy private pool

## Current pool

- Alive now: 1389
- Gold now: 450
- HTTP: 508 alive / 110 gold
- HTTPS: 382 alive / 32 gold
- SOCKS4: 242 alive / 149 gold
- SOCKS5: 257 alive / 159 gold

## Historical pool

- Discovered: 160009
- Ever alive: 30502
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
