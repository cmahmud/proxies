# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 396
- HTTP: 326 alive / 93 gold
- HTTPS: 216 alive / 20 gold
- SOCKS4: 195 alive / 125 gold
- SOCKS5: 268 alive / 158 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32149
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
