# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 417
- HTTP: 104 alive / 75 gold
- HTTPS: 62 alive / 18 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33715
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
