# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 391
- HTTP: 122 alive / 65 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 175 alive / 154 gold
- SOCKS5: 187 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33132
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
