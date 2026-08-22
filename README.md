# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 345
- HTTP: 271 alive / 75 gold
- HTTPS: 171 alive / 20 gold
- SOCKS4: 191 alive / 119 gold
- SOCKS5: 223 alive / 131 gold

## Historical pool

- Discovered: 167924
- Ever alive: 32593
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
