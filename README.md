# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 381
- HTTP: 109 alive / 60 gold
- HTTPS: 33 alive / 8 gold
- SOCKS4: 187 alive / 155 gold
- SOCKS5: 203 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33087
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
