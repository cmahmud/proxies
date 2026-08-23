# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 395
- HTTP: 116 alive / 64 gold
- HTTPS: 53 alive / 15 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 192 alive / 162 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33147
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
