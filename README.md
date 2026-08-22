# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 421
- HTTP: 324 alive / 91 gold
- HTTPS: 220 alive / 27 gold
- SOCKS4: 199 alive / 144 gold
- SOCKS5: 238 alive / 159 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31561
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
