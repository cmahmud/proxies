# SyndProxy private pool

## Current pool

- Alive now: 707
- Gold now: 249
- HTTP: 169 alive / 27 gold
- HTTPS: 151 alive / 8 gold
- SOCKS4: 181 alive / 112 gold
- SOCKS5: 206 alive / 102 gold

## Historical pool

- Discovered: 95261
- Ever alive: 10224
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
