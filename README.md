# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 372
- HTTP: 90 alive / 56 gold
- HTTPS: 34 alive / 9 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 188 alive / 155 gold

## Historical pool

- Discovered: 174819
- Ever alive: 33102
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
