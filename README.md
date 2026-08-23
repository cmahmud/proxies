# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 377
- HTTP: 93 alive / 57 gold
- HTTPS: 36 alive / 9 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 184 alive / 157 gold

## Historical pool

- Discovered: 174819
- Ever alive: 33103
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
