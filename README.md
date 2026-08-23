# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 382
- HTTP: 111 alive / 60 gold
- HTTPS: 32 alive / 8 gold
- SOCKS4: 183 alive / 155 gold
- SOCKS5: 202 alive / 159 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33087
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
