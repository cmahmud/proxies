# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 375
- HTTP: 110 alive / 58 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 162 alive / 153 gold
- SOCKS5: 172 alive / 154 gold

## Historical pool

- Discovered: 174309
- Ever alive: 33084
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
