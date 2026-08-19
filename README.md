# SyndProxy private pool

## Current pool

- Alive now: 1319
- Gold now: 531
- HTTP: 512 alive / 189 gold
- HTTPS: 335 alive / 47 gold
- SOCKS4: 228 alive / 135 gold
- SOCKS5: 244 alive / 160 gold

## Historical pool

- Discovered: 125596
- Ever alive: 19575
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
