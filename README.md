# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 437
- HTTP: 381 alive / 112 gold
- HTTPS: 262 alive / 30 gold
- SOCKS4: 228 alive / 151 gold
- SOCKS5: 247 alive / 144 gold

## Historical pool

- Discovered: 160018
- Ever alive: 30516
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
