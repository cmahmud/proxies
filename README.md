# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 417
- HTTP: 97 alive / 75 gold
- HTTPS: 125 alive / 20 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42048
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
