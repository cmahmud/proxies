# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 422
- HTTP: 105 alive / 64 gold
- HTTPS: 88 alive / 23 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 197 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35755
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
