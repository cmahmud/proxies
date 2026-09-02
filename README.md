# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 440
- HTTP: 138 alive / 76 gold
- HTTPS: 114 alive / 29 gold
- SOCKS4: 187 alive / 164 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47642
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
