# SyndProxy private pool

## Current pool

- Alive now: 1723
- Gold now: 629
- HTTP: 688 alive / 237 gold
- HTTPS: 527 alive / 129 gold
- SOCKS4: 189 alive / 100 gold
- SOCKS5: 319 alive / 163 gold

## Historical pool

- Discovered: 143105
- Ever alive: 24680
- Ever gold: 1031

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
