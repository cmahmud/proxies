# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 402
- HTTP: 305 alive / 91 gold
- HTTPS: 208 alive / 25 gold
- SOCKS4: 217 alive / 136 gold
- SOCKS5: 243 alive / 150 gold

## Historical pool

- Discovered: 164248
- Ever alive: 32105
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
