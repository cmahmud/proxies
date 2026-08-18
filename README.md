# SyndProxy private pool

## Current pool

- Alive now: 706
- Gold now: 208
- HTTP: 176 alive / 21 gold
- HTTPS: 123 alive / 9 gold
- SOCKS4: 203 alive / 97 gold
- SOCKS5: 204 alive / 81 gold

## Historical pool

- Discovered: 87994
- Ever alive: 7994
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
