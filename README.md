# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 389
- HTTP: 357 alive / 86 gold
- HTTPS: 231 alive / 26 gold
- SOCKS4: 187 alive / 113 gold
- SOCKS5: 257 alive / 164 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32451
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
