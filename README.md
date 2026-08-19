# SyndProxy private pool

## Current pool

- Alive now: 1424
- Gold now: 395
- HTTP: 521 alive / 97 gold
- HTTPS: 362 alive / 22 gold
- SOCKS4: 228 alive / 133 gold
- SOCKS5: 313 alive / 143 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22506
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
