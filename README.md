# SyndProxy private pool

## Current pool

- Alive now: 1672
- Gold now: 597
- HTTP: 630 alive / 208 gold
- HTTPS: 540 alive / 110 gold
- SOCKS4: 208 alive / 135 gold
- SOCKS5: 294 alive / 144 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23862
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
