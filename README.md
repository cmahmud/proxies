# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 359
- HTTP: 266 alive / 51 gold
- HTTPS: 208 alive / 16 gold
- SOCKS4: 230 alive / 148 gold
- SOCKS5: 250 alive / 144 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14752
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
