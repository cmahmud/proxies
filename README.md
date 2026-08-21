# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 366
- HTTP: 289 alive / 81 gold
- HTTPS: 228 alive / 21 gold
- SOCKS4: 185 alive / 115 gold
- SOCKS5: 243 alive / 149 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29860
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
