# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 377
- HTTP: 101 alive / 57 gold
- HTTPS: 31 alive / 8 gold
- SOCKS4: 188 alive / 154 gold
- SOCKS5: 200 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33087
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
