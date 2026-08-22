# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 399
- HTTP: 361 alive / 90 gold
- HTTPS: 217 alive / 25 gold
- SOCKS4: 228 alive / 136 gold
- SOCKS5: 247 alive / 148 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32097
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
