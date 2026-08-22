# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 382
- HTTP: 233 alive / 87 gold
- HTTPS: 171 alive / 28 gold
- SOCKS4: 211 alive / 138 gold
- SOCKS5: 216 alive / 129 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31628
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
