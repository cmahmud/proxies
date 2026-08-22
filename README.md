# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 383
- HTTP: 301 alive / 81 gold
- HTTPS: 228 alive / 23 gold
- SOCKS4: 209 alive / 124 gold
- SOCKS5: 251 alive / 155 gold

## Historical pool

- Discovered: 164912
- Ever alive: 32135
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
