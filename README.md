# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 372
- HTTP: 255 alive / 67 gold
- HTTPS: 190 alive / 23 gold
- SOCKS4: 206 alive / 125 gold
- SOCKS5: 230 alive / 157 gold

## Historical pool

- Discovered: 164971
- Ever alive: 32251
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
