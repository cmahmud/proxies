# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 242
- HTTP: 358 alive / 36 gold
- HTTPS: 160 alive / 8 gold
- SOCKS4: 241 alive / 132 gold
- SOCKS5: 195 alive / 66 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9659
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
