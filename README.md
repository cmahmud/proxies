# SyndProxy private pool

## Current pool

- Alive now: 1815
- Gold now: 691
- HTTP: 684 alive / 237 gold
- HTTPS: 584 alive / 147 gold
- SOCKS4: 222 alive / 143 gold
- SOCKS5: 325 alive / 164 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24482
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
