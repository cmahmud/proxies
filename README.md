# SyndProxy private pool

## Current pool

- Alive now: 789
- Gold now: 399
- HTTP: 211 alive / 92 gold
- HTTPS: 142 alive / 27 gold
- SOCKS4: 208 alive / 144 gold
- SOCKS5: 228 alive / 136 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31796
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
