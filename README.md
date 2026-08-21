# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 365
- HTTP: 302 alive / 77 gold
- HTTPS: 173 alive / 19 gold
- SOCKS4: 190 alive / 128 gold
- SOCKS5: 218 alive / 141 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29669
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
