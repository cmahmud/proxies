# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 385
- HTTP: 384 alive / 87 gold
- HTTPS: 238 alive / 22 gold
- SOCKS4: 192 alive / 113 gold
- SOCKS5: 263 alive / 163 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32451
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
