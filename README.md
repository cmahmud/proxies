# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 369
- HTTP: 175 alive / 67 gold
- HTTPS: 144 alive / 19 gold
- SOCKS4: 192 alive / 121 gold
- SOCKS5: 243 alive / 162 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26093
- Ever gold: 1078

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
