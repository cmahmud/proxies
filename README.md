# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 412
- HTTP: 295 alive / 83 gold
- HTTPS: 225 alive / 25 gold
- SOCKS4: 190 alive / 135 gold
- SOCKS5: 266 alive / 169 gold

## Historical pool

- Discovered: 161927
- Ever alive: 31198
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
