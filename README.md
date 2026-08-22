# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 378
- HTTP: 305 alive / 81 gold
- HTTPS: 218 alive / 20 gold
- SOCKS4: 200 alive / 123 gold
- SOCKS5: 258 alive / 154 gold

## Historical pool

- Discovered: 164912
- Ever alive: 32137
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
