# SyndProxy private pool

## Current pool

- Alive now: 756
- Gold now: 359
- HTTP: 228 alive / 82 gold
- HTTPS: 160 alive / 18 gold
- SOCKS4: 199 alive / 144 gold
- SOCKS5: 169 alive / 115 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25334
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
