# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 343
- HTTP: 157 alive / 39 gold
- HTTPS: 68 alive / 9 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 190 alive / 144 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32841
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
