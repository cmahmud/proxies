# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 371
- HTTP: 343 alive / 77 gold
- HTTPS: 218 alive / 21 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 245 alive / 137 gold

## Historical pool

- Discovered: 144770
- Ever alive: 25299
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
