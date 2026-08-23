# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 380
- HTTP: 107 alive / 60 gold
- HTTPS: 36 alive / 8 gold
- SOCKS4: 186 alive / 154 gold
- SOCKS5: 204 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33087
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
