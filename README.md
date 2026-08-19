# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 479
- HTTP: 361 alive / 126 gold
- HTTPS: 263 alive / 76 gold
- SOCKS4: 210 alive / 123 gold
- SOCKS5: 213 alive / 154 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17888
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
