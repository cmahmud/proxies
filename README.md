# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 256
- HTTP: 319 alive / 33 gold
- HTTPS: 191 alive / 9 gold
- SOCKS4: 241 alive / 144 gold
- SOCKS5: 168 alive / 70 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13723
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
