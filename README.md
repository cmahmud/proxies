# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 378
- HTTP: 274 alive / 73 gold
- HTTPS: 175 alive / 24 gold
- SOCKS4: 192 alive / 124 gold
- SOCKS5: 227 alive / 157 gold

## Historical pool

- Discovered: 164972
- Ever alive: 32254
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
