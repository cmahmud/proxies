# SyndProxy private pool

## Current pool

- Alive now: 1174
- Gold now: 392
- HTTP: 384 alive / 97 gold
- HTTPS: 294 alive / 26 gold
- SOCKS4: 241 alive / 133 gold
- SOCKS5: 255 alive / 136 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25117
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
