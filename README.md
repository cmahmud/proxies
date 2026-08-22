# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 404
- HTTP: 256 alive / 97 gold
- HTTPS: 191 alive / 30 gold
- SOCKS4: 234 alive / 145 gold
- SOCKS5: 245 alive / 132 gold

## Historical pool

- Discovered: 161992
- Ever alive: 31310
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
