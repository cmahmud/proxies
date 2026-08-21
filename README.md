# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 419
- HTTP: 316 alive / 96 gold
- HTTPS: 215 alive / 23 gold
- SOCKS4: 242 alive / 144 gold
- SOCKS5: 269 alive / 156 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28154
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
