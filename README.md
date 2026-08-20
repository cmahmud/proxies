# SyndProxy private pool

## Current pool

- Alive now: 1594
- Gold now: 627
- HTTP: 537 alive / 210 gold
- HTTPS: 463 alive / 117 gold
- SOCKS4: 230 alive / 144 gold
- SOCKS5: 364 alive / 156 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24063
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
