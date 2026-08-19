# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 505
- HTTP: 379 alive / 170 gold
- HTTPS: 250 alive / 48 gold
- SOCKS4: 232 alive / 143 gold
- SOCKS5: 220 alive / 144 gold

## Historical pool

- Discovered: 124827
- Ever alive: 19167
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
