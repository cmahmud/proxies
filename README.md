# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 427
- HTTP: 300 alive / 89 gold
- HTTPS: 244 alive / 31 gold
- SOCKS4: 209 alive / 143 gold
- SOCKS5: 245 alive / 164 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31240
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
