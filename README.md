# SyndProxy private pool

## Current pool

- Alive now: 1653
- Gold now: 588
- HTTP: 618 alive / 198 gold
- HTTPS: 465 alive / 100 gold
- SOCKS4: 259 alive / 138 gold
- SOCKS5: 311 alive / 152 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23336
- Ever gold: 918

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
