# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 321
- HTTP: 259 alive / 58 gold
- HTTPS: 178 alive / 13 gold
- SOCKS4: 202 alive / 125 gold
- SOCKS5: 204 alive / 125 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20058
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
