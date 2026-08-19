# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 521
- HTTP: 318 alive / 146 gold
- HTTPS: 264 alive / 88 gold
- SOCKS4: 225 alive / 150 gold
- SOCKS5: 214 alive / 137 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17611
- Ever gold: 691

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
