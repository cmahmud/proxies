# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 317
- HTTP: 359 alive / 41 gold
- HTTPS: 183 alive / 11 gold
- SOCKS4: 243 alive / 137 gold
- SOCKS5: 235 alive / 128 gold

## Historical pool

- Discovered: 107043
- Ever alive: 14386
- Ever gold: 441

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
