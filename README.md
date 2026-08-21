# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 392
- HTTP: 250 alive / 91 gold
- HTTPS: 188 alive / 19 gold
- SOCKS4: 190 alive / 137 gold
- SOCKS5: 224 alive / 145 gold

## Historical pool

- Discovered: 152163
- Ever alive: 27865
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
