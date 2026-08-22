# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 414
- HTTP: 283 alive / 84 gold
- HTTPS: 233 alive / 24 gold
- SOCKS4: 195 alive / 136 gold
- SOCKS5: 256 alive / 170 gold

## Historical pool

- Discovered: 161927
- Ever alive: 31201
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
