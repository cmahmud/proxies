# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 526
- HTTP: 450 alive / 159 gold
- HTTPS: 249 alive / 81 gold
- SOCKS4: 210 alive / 136 gold
- SOCKS5: 246 alive / 150 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18763
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
