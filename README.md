# SyndProxy private pool

## Current pool

- Alive now: 784
- Gold now: 405
- HTTP: 219 alive / 89 gold
- HTTPS: 167 alive / 24 gold
- SOCKS4: 183 alive / 137 gold
- SOCKS5: 215 alive / 155 gold

## Historical pool

- Discovered: 162444
- Ever alive: 31449
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
