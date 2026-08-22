# SyndProxy private pool

## Current pool

- Alive now: 756
- Gold now: 409
- HTTP: 197 alive / 91 gold
- HTTPS: 157 alive / 25 gold
- SOCKS4: 185 alive / 138 gold
- SOCKS5: 217 alive / 155 gold

## Historical pool

- Discovered: 162443
- Ever alive: 31444
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
