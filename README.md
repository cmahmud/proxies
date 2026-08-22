# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 419
- HTTP: 344 alive / 96 gold
- HTTPS: 292 alive / 32 gold
- SOCKS4: 202 alive / 133 gold
- SOCKS5: 235 alive / 158 gold

## Historical pool

- Discovered: 161017
- Ever alive: 31100
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
