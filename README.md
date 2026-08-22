# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 430
- HTTP: 317 alive / 96 gold
- HTTPS: 225 alive / 36 gold
- SOCKS4: 186 alive / 127 gold
- SOCKS5: 269 alive / 171 gold

## Historical pool

- Discovered: 161922
- Ever alive: 31156
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
