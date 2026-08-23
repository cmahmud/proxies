# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 376
- HTTP: 92 alive / 57 gold
- HTTPS: 34 alive / 9 gold
- SOCKS4: 166 alive / 153 gold
- SOCKS5: 183 alive / 157 gold

## Historical pool

- Discovered: 174819
- Ever alive: 33102
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
