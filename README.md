# SyndProxy private pool

## Current pool

- Alive now: 1683
- Gold now: 639
- HTTP: 725 alive / 237 gold
- HTTPS: 531 alive / 135 gold
- SOCKS4: 182 alive / 103 gold
- SOCKS5: 245 alive / 164 gold

## Historical pool

- Discovered: 143423
- Ever alive: 24686
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
