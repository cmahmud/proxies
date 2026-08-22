# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 375
- HTTP: 269 alive / 82 gold
- HTTPS: 233 alive / 26 gold
- SOCKS4: 231 alive / 125 gold
- SOCKS5: 230 alive / 142 gold

## Historical pool

- Discovered: 164253
- Ever alive: 32115
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
