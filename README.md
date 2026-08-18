# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 254
- HTTP: 213 alive / 31 gold
- HTTPS: 117 alive / 7 gold
- SOCKS4: 230 alive / 124 gold
- SOCKS5: 231 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9087
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
