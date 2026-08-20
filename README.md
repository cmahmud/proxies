# SyndProxy private pool

## Current pool

- Alive now: 1578
- Gold now: 638
- HTTP: 593 alive / 216 gold
- HTTPS: 508 alive / 119 gold
- SOCKS4: 238 alive / 157 gold
- SOCKS5: 239 alive / 146 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23758
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
