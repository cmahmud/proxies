# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 425
- HTTP: 117 alive / 80 gold
- HTTPS: 166 alive / 16 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42307
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
