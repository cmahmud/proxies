# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 393
- HTTP: 119 alive / 64 gold
- HTTPS: 55 alive / 15 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33146
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
