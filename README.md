# SyndProxy private pool

## Current pool

- Alive now: 694
- Gold now: 393
- HTTP: 167 alive / 83 gold
- HTTPS: 117 alive / 21 gold
- SOCKS4: 208 alive / 143 gold
- SOCKS5: 202 alive / 146 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25223
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
