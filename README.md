# SyndProxy private pool

## Current pool

- Alive now: 726
- Gold now: 387
- HTTP: 161 alive / 69 gold
- HTTPS: 131 alive / 18 gold
- SOCKS4: 223 alive / 146 gold
- SOCKS5: 211 alive / 154 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26015
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
