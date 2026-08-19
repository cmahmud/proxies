# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 320
- HTTP: 307 alive / 49 gold
- HTTPS: 181 alive / 10 gold
- SOCKS4: 202 alive / 131 gold
- SOCKS5: 198 alive / 130 gold

## Historical pool

- Discovered: 128086
- Ever alive: 20031
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
