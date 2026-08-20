# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 378
- HTTP: 184 alive / 74 gold
- HTTPS: 162 alive / 20 gold
- SOCKS4: 203 alive / 149 gold
- SOCKS5: 204 alive / 135 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26145
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
