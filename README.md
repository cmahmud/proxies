# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 379
- HTTP: 103 alive / 59 gold
- HTTPS: 32 alive / 8 gold
- SOCKS4: 189 alive / 154 gold
- SOCKS5: 192 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33087
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
