# SyndProxy private pool

## Current pool

- Alive now: 1820
- Gold now: 689
- HTTP: 692 alive / 238 gold
- HTTPS: 589 alive / 145 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 323 alive / 163 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24485
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
