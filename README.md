# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 307
- HTTP: 161 alive / 37 gold
- HTTPS: 54 alive / 11 gold
- SOCKS4: 191 alive / 153 gold
- SOCKS5: 190 alive / 106 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32833
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
