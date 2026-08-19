# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 329
- HTTP: 288 alive / 57 gold
- HTTPS: 200 alive / 8 gold
- SOCKS4: 234 alive / 142 gold
- SOCKS5: 219 alive / 122 gold

## Historical pool

- Discovered: 129271
- Ever alive: 20256
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
