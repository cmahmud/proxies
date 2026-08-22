# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 399
- HTTP: 314 alive / 91 gold
- HTTPS: 236 alive / 25 gold
- SOCKS4: 225 alive / 137 gold
- SOCKS5: 247 alive / 146 gold

## Historical pool

- Discovered: 164248
- Ever alive: 32107
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
