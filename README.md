# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 354
- HTTP: 301 alive / 50 gold
- HTTPS: 199 alive / 16 gold
- SOCKS4: 228 alive / 147 gold
- SOCKS5: 236 alive / 141 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14794
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
