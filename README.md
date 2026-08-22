# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 378
- HTTP: 272 alive / 83 gold
- HTTPS: 143 alive / 23 gold
- SOCKS4: 183 alive / 119 gold
- SOCKS5: 223 alive / 153 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32389
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
