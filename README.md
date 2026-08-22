# SyndProxy private pool

## Current pool

- Alive now: 1119
- Gold now: 404
- HTTP: 394 alive / 86 gold
- HTTPS: 245 alive / 25 gold
- SOCKS4: 226 alive / 150 gold
- SOCKS5: 254 alive / 143 gold

## Historical pool

- Discovered: 165734
- Ever alive: 32284
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
