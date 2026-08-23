# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 378
- HTTP: 112 alive / 59 gold
- HTTPS: 35 alive / 8 gold
- SOCKS4: 174 alive / 153 gold
- SOCKS5: 191 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33087
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
