# SyndProxy private pool

## Current pool

- Alive now: 1353
- Gold now: 437
- HTTP: 474 alive / 99 gold
- HTTPS: 307 alive / 26 gold
- SOCKS4: 252 alive / 148 gold
- SOCKS5: 320 alive / 164 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22453
- Ever gold: 901

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
