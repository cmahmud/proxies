# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 376
- HTTP: 184 alive / 72 gold
- HTTPS: 148 alive / 21 gold
- SOCKS4: 205 alive / 147 gold
- SOCKS5: 204 alive / 136 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26145
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
