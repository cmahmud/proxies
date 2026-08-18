# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 356
- HTTP: 268 alive / 52 gold
- HTTPS: 205 alive / 16 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 242 alive / 141 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14760
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
