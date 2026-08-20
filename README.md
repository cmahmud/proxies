# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 388
- HTTP: 200 alive / 77 gold
- HTTPS: 113 alive / 21 gold
- SOCKS4: 228 alive / 143 gold
- SOCKS5: 208 alive / 147 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25253
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
