# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 440
- HTTP: 136 alive / 75 gold
- HTTPS: 115 alive / 29 gold
- SOCKS4: 188 alive / 165 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47640
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
