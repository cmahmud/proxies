# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 417
- HTTP: 273 alive / 83 gold
- HTTPS: 240 alive / 26 gold
- SOCKS4: 198 alive / 136 gold
- SOCKS5: 253 alive / 172 gold

## Historical pool

- Discovered: 161927
- Ever alive: 31202
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
