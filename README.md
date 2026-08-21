# SyndProxy private pool

## Current pool

- Alive now: 933
- Gold now: 402
- HTTP: 265 alive / 96 gold
- HTTPS: 227 alive / 27 gold
- SOCKS4: 233 alive / 155 gold
- SOCKS5: 208 alive / 124 gold

## Historical pool

- Discovered: 160982
- Ever alive: 30860
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
