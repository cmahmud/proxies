# SyndProxy private pool

## Current pool

- Alive now: 860
- Gold now: 400
- HTTP: 228 alive / 98 gold
- HTTPS: 202 alive / 30 gold
- SOCKS4: 196 alive / 141 gold
- SOCKS5: 234 alive / 131 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31785
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
