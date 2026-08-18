# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 349
- HTTP: 399 alive / 50 gold
- HTTPS: 213 alive / 14 gold
- SOCKS4: 228 alive / 141 gold
- SOCKS5: 243 alive / 144 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14856
- Ever gold: 475

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
