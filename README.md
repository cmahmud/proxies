# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 402
- HTTP: 268 alive / 80 gold
- HTTPS: 209 alive / 29 gold
- SOCKS4: 210 alive / 127 gold
- SOCKS5: 247 alive / 166 gold

## Historical pool

- Discovered: 164962
- Ever alive: 32241
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
