# SyndProxy validated proxy pool

## Current pool

- Alive now: 426
- Gold now: 362
- HTTP: 63 alive / 41 gold
- HTTPS: 27 alive / 11 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 174 alive / 155 gold

## Historical pool

- Discovered: 173751
- Ever alive: 33023
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
