# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 403
- HTTP: 195 alive / 86 gold
- HTTPS: 109 alive / 16 gold
- SOCKS4: 216 alive / 149 gold
- SOCKS5: 221 alive / 152 gold

## Historical pool

- Discovered: 155785
- Ever alive: 29299
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
