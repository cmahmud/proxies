# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 395
- HTTP: 202 alive / 82 gold
- HTTPS: 111 alive / 16 gold
- SOCKS4: 222 alive / 148 gold
- SOCKS5: 225 alive / 149 gold

## Historical pool

- Discovered: 155787
- Ever alive: 29309
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
