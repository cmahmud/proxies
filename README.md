# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 423
- HTTP: 303 alive / 87 gold
- HTTPS: 218 alive / 28 gold
- SOCKS4: 202 alive / 142 gold
- SOCKS5: 255 alive / 166 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31234
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
