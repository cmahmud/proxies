# SyndProxy private pool

## Current pool

- Alive now: 1873
- Gold now: 618
- HTTP: 821 alive / 239 gold
- HTTPS: 619 alive / 114 gold
- SOCKS4: 183 alive / 103 gold
- SOCKS5: 250 alive / 162 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24768
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
