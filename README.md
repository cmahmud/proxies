# SyndProxy private pool

## Current pool

- Alive now: 1057
- Gold now: 538
- HTTP: 362 alive / 161 gold
- HTTPS: 244 alive / 95 gold
- SOCKS4: 242 alive / 146 gold
- SOCKS5: 209 alive / 136 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18891
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
